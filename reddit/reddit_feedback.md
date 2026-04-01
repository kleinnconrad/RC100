# Reddit Feedback: RC100 Project

**Original Post:** [Link zum Thread](https://www.reddit.com/r/rccars/comments/1s8nl1m/)
**Letzter Sync:** 01.04.2026 14:19:23

---

**u/Basic-You7791** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/):
> Hey 
> r/rccars
> ! 👋 We’re complete newbies to the hobby, but we jumped right in with a small family project. The Goal: Build a budget-friendly 1:10 RC car (Carten T410R chassis as it turned out after researching) that can repeatedly hit 100 km/h (62 mph) without breaking. Instead of just throwing the first suggested components at it, we tried to take a "well-engineered" approach to "playfully" introduce our kids to structured problem-solving. We used specs, thermal/gear calculations, Architecture Decision Records (ADRs), BOM etc. for the build. On top of that, we’re trying to turn the car into a smart IoT device that live-streams its own telemetry data during speed runs! We documented everything on GitHub. Quick apology: The repos are in German! And we are unfortunately not done yet. We did a lot of beginners mistakes that still needs to be fixed.
>  
> Main Build (Specs, ADRs, Calculators): 
> https://github.com/kleinnconrad/RC100
>  IoT: 
> https://github.com/kleinnconrad/carten_telemetrie
>  
> We'd love to hear your thoughts or tips for complete beginners.
>  
>    submitted by   
>  /u/Basic-You7791 
>  
>  
> [link]
>  
> [comments]

---

**u/Show_Kitchen** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odi7mgq/):
> Cool project. How old are your kids? I also do “engineering projects for the kids” but I’m the kid. 
>  
> Three speed tips: they make speed-run wheels and tires that are more aero and handle better at speed. 
>  
> The body can be a major limiter. At high speed the edges can start flapping. It’s a good idea to attach a camera for test runs to see what’s flapping then reinforce with drywall tape. I foresee that wing on the back causing problems. 
>  
> Also, at high speed it’s often easier to steer using the trim adjust instead of the steering wheel so you don’t accidentally over-cook it.
>  
> Have fun!

---

**u/Basic-You7791** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odiapbm/):
> Thanks for the hints! We'll look into that. The kid's are 6 and 4. We involve them on appropriate level so they can follow and contribute. Esp. we discuss with the kids that parts have required properties (specs) and that there are mostly several options to choose from (ADR's). We show the parts to them (from the vendor sites), explain what they do and how they are different from each other and discuss and decide together what would be best. Also the kids can help with the building. Ofc the 4 year old is still limited but he can already often get the point. The reflection of the elaborations on GitHub is something we will hand to them later. Till then they know that everything we discuss, decide and do will be "put to the Internet". What they like best is doing testing with the car ofc😄.

---

**u/Show_Kitchen** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odicll4/):
> Right on! I got matching trx4s for me and my 5yo and we go for long adventures in the woods. This summer I’m hoping to introduce him to the fast RCs. It’s a great excuse to do the things I want to do anyway, but now I got a little buddy to take with me.

---

**u/a1rwav3** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odj3ssp/):
> True, get some Hudy A36. They are cheap and built to resist to high speed (at least under 140km/h).
>  
> https://preview.redd.it/wrfajdy2tesg1.jpeg?width=381&format=pjpg&auto=webp&s=118b5b34c8e4f32ab2235d7d8d2d42604146bc2e

---

**u/bigrroberto** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odi6uxl/):
> I don’t have any advice as I’m new too, but this sounds like a cool project. 
>  
> Kudos to you for involving the kids like this it’s a neat way to integrate science and technology into fun.

---

**u/aintwrongthou** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odi9e7i/):
> That’s Mega cool! Have fun! If you have the chance, see if there are races around your area, now that the outdoor season is upon us and look out for the „modified“ class, they might be the fastest of the bunch.

---

**u/a1rwav3** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odj3bmi/):
> The choice of the platform is good. Even if it is not a very performant car, the fact that most of the transmission can be in steel is an advantage.
>  
> You should easily reach this speed with a proper esc in 2s. Modern 10.5T brushless motors with dynamic timing can easily reach 130km/h.
>  
> Just one advice, don't hesitate to use D/R on steering for speedruns, it will make the car more stable. And you should probably get rid of the servo saver for speedruns. If this thing start to oscillate at high speed it will result in a hard crash.

---

**u/Basic-You7791** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odj83hp/):
> We use a 3660 / 3700 KV Motor with a 120A ESC and 3S Lipo. We opted for this because we wanted to increase the gear ratio rather than using high RPM of the motor. We hope this prevents us from overheating. First RPM test (without load / using Laser RPM measurement) showed a theoretical topspeed of 135 km/h.

---

**u/a1rwav3** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odj8gp1/):
> Sadly that's not how brushless motors work... Most of them have a small windows for gear ratio, especially with fixed timing. But if you are really committed to speed runs it shouldn't be an issue, as it won't run for 5 minutes straight.

---

**u/Basic-You7791** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odjbyx5/):
> It's 43t pinion gear on 72t main gear. Afaik a 3660 can handle this more effective than a 3650 due to higher torque. With a 3650 it would have been necessary to use a smaller pinion gear and compensate with more RPM. Means the 43t set up will need less RPM to achieve a given speed but needs more torque to handle the ratio and vice versa

---

**u/a1rwav3** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odjlr04/):
> What kind of final ratio are going for? 1:4.0?

---

**u/Basic-You7791** [schrieb](https://www.reddit.com/r/rccars/comments/1s8nl1m/build_first_rc_project_engineering_a_budget/odjqlsu/):
> It's 4.13

---

