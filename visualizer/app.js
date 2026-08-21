document.addEventListener('DOMContentLoaded', async () => {
    // Navigation Logic
    const navBtns = document.querySelectorAll('.nav-btn');
    const views = document.querySelectorAll('.view-container');
    const viewTitle = document.getElementById('view-title');

    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            navBtns.forEach(b => b.classList.remove('active'));
            views.forEach(v => v.classList.remove('active'));
            
            btn.classList.add('active');
            const targetView = btn.getAttribute('data-view');
            document.getElementById(`${targetView}-view`).classList.add('active');
            
            viewTitle.textContent = targetView === 'adrs' ? 'Architecture Decision Records' : 'System Specifications';
        });
    });

    // Data Fetching
    const repoBaseUrl = 'https://raw.githubusercontent.com/kleinnconrad/RC100/main';
    const adrFiles = [
        'adr_akku.yaml', 'adr_body.yaml', 'adr_brushless.yaml', 'adr_chassis.yaml',
        'adr_fernsteuerung.yaml', 'adr_gps.yaml', 'adr_ladegeraet.yaml',
        'adr_lenkservo.yaml', 'adr_motorkuehlung.yaml', 'adr_reifen.yaml'
    ];

    let fullSpecData = null;
    let adrData = [];

    async function loadData() {
        try {
            // Load Full Spec
            const specRes = await fetch(`${repoBaseUrl}/full_spec.yaml`);
            if (specRes.ok) {
                const specText = await specRes.text();
                fullSpecData = jsyaml.load(specText);
            }

            // Load ADRs
            const adrPromises = adrFiles.map(file => fetch(`${repoBaseUrl}/architektur/${file}`).then(res => res.text()));
            const adrTexts = await Promise.all(adrPromises);
            
            adrData = adrTexts.map(text => {
                try {
                    return jsyaml.load(text);
                } catch(e) {
                    return null;
                }
            }).filter(Boolean).map(doc => doc.adr || doc);

            renderADRs();
            renderSpecs();

            // Hide Loader
            const loader = document.getElementById('loader');
            loader.style.opacity = '0';
            setTimeout(() => loader.style.display = 'none', 500);

        } catch (error) {
            console.error('Error loading YAML data:', error);
            document.getElementById('loader').innerHTML = '<p style="color:var(--danger)">Fehler beim Laden der Daten.</p>';
        }
    }

    // Render ADRs
    function renderADRs() {
        const grid = document.getElementById('adr-grid');
        grid.innerHTML = '';

        adrData.forEach(adr => {
            const statusClass = adr.status ? `status-${adr.status.toLowerCase().replace(/\s+/g, '-')}` : '';
            
            const card = document.createElement('div');
            card.className = 'adr-card';
            card.innerHTML = `
                <div class="adr-header">
                    <span class="adr-id">${adr.id || 'N/A'}</span>
                    <span class="adr-status ${statusClass}">${adr.status || 'Unknown'}</span>
                </div>
                <h3 class="adr-title">${adr.title || 'Untitled'}</h3>
                <div class="adr-context">${adr.context || ''}</div>
            `;
            
            card.addEventListener('click', () => {
                // Future expansion: Show modal with full ADR details
                alert(`ADR: ${adr.title}\n\nKontext: ${adr.context?.substring(0, 100)}...`);
            });

            grid.appendChild(card);
        });
    }

    // Render Specs
    function renderSpecs() {
        const nav = document.getElementById('spec-nav');
        if (!fullSpecData) return;

        // Group by top-level keys
        const categories = Object.keys(fullSpecData);
        nav.innerHTML = '';

        categories.forEach(category => {
            const catDiv = document.createElement('div');
            catDiv.className = 'spec-category';
            catDiv.innerHTML = `<h3 class="spec-category-title">${category}</h3>`;
            
            const list = document.createElement('ul');
            list.className = 'spec-list';

            // Iterate over items in category
            const items = fullSpecData[category];
            if (typeof items === 'object' && items !== null) {
                Object.keys(items).forEach(itemName => {
                    const li = document.createElement('li');
                    li.className = 'spec-item';
                    li.textContent = itemName;
                    
                    li.addEventListener('click', () => {
                        document.querySelectorAll('.spec-item').forEach(el => el.classList.remove('active'));
                        li.classList.add('active');
                        renderSpecDetails(itemName, items[itemName]);
                    });

                    list.appendChild(li);
                });
            }

            catDiv.appendChild(list);
            nav.appendChild(catDiv);
        });
    }

    function renderSpecDetails(name, data) {
        const detailsContainer = document.getElementById('spec-details');
        
        let html = `<div class="detail-view">
            <h3>${name.replace(/_/g, ' ').toUpperCase()}</h3>`;

        if (typeof data === 'object' && data !== null) {
            Object.keys(data).forEach(groupName => {
                html += `<div class="property-group">
                    <h4>${groupName.replace(/_/g, ' ')}</h4>
                    <div class="property-grid">`;
                
                const props = data[groupName];
                if (typeof props === 'object' && props !== null) {
                    Object.keys(props).forEach(propKey => {
                        let val = props[propKey];
                        if (typeof val === 'object') val = JSON.stringify(val);
                        
                        html += `
                        <div class="property-item">
                            <div class="property-label">${propKey.replace(/_/g, ' ')}</div>
                            <div class="property-value">${val}</div>
                        </div>`;
                    });
                } else {
                    html += `<div class="property-item"><div class="property-value">${props}</div></div>`;
                }
                
                html += `</div></div>`;
            });
        }
        
        html += `</div>`;
        detailsContainer.innerHTML = html;
    }

    // Initialize
    loadData();
});
