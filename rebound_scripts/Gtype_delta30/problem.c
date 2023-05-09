#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include "rebound.h"

// Define our own collision resolve function, which will only record collisions but not change any of the particles.
int collision_record_only(struct reb_simulation* const r, struct reb_collision c){

    struct reb_particle* particles = r->particles;
    struct reb_particle primary = r->particles[0];
    const double t = r->t;

    int result = reb_collision_resolve_merge(r, c);

    if (c.p1 == 1 || c.p2 == 1) {
        
        if (c.p1 == 1) {
            struct reb_orbit o = reb_tools_particle_to_orbit(r->G, particles[c.p2], primary);

            FILE* ofae = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_ae_particle3.txt","a+");        // open file for collision output
            fprintf(ofae, "%e\t", t);
            fprintf(ofae, "%d\t", particles[c.p2].hash);                    // time, hash
            fprintf(ofae, "%e %e %e\t", o.a, o.e, o.inc);    // relative velocity
            fprintf(ofae, "\n");
            fclose(ofae);

            double vx_tp = particles[c.p2].vx;
            double vy_tp = particles[c.p2].vy;
            double vz_tp = particles[c.p2].vz;

            double vx_p = particles[c.p1].vx;
            double vy_p = particles[c.p1].vy;
            double vz_p = particles[c.p1].vz;

            double rel_vel = pow(pow(vx_tp-vx_p, 2.) + pow(vy_tp-vy_p, 2.) + pow(vz_tp-vz_p, 2.), 1./2.);
            double tp_vel = pow(pow(vx_tp, 2.) + pow(vy_tp, 2.) + pow(vz_tp, 2.), 1./2.);
            double plan_vel = pow(pow(vx_p, 2.) + pow(vy_p, 2.) + pow(vz_p, 2.), 1./2.);

            FILE* of = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_velocities_particle3.txt","a+");        // open file for collision output
            fprintf(of, "%e\t", t);                    // time
            fprintf(of, "%e %e %e\t", rel_vel, tp_vel,plan_vel);    // relative velocity
            fprintf(of, "\n");
            fclose(of);                        // close file

            return 2;
        }
        else if (c.p2 == 1) {
            struct reb_orbit o = reb_tools_particle_to_orbit(r->G, particles[c.p1], primary);

            FILE* ofae = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_ae_particle3.txt","a+");        // open file for collision output
            fprintf(ofae, "%e\t", t);
            fprintf(ofae, "%d\t", particles[c.p1].hash);                    // time, hash
            fprintf(ofae, "%e %e %e\t", o.a, o.e, o.inc);    // relative velocity
            fprintf(ofae, "\n");
            fclose(ofae);

            double vx_tp = particles[c.p1].vx;
            double vy_tp = particles[c.p1].vy;
            double vz_tp = particles[c.p1].vz;

            double vx_p = particles[c.p2].vx;
            double vy_p = particles[c.p2].vy;
            double vz_p = particles[c.p2].vz;

            double rel_vel = pow(pow(vx_tp-vx_p, 2.) + pow(vy_tp-vy_p, 2.) + pow(vz_tp-vz_p, 2.), 1./2.);
            double tp_vel = pow(pow(vx_tp, 2.) + pow(vy_tp, 2.) + pow(vz_tp, 2.), 1./2.);
            double plan_vel = pow(pow(vx_p, 2.) + pow(vy_p, 2.) + pow(vz_p, 2.), 1./2.);

            FILE* of = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_velocities_particle3.txt","a+");        // open file for collision output
            fprintf(of, "%e\t", t);                    // time
            fprintf(of, "%e %e %e\t", rel_vel, tp_vel, plan_vel);    // relative velocity
            fprintf(of, "\n");
            fclose(of);                        // close file

            return 1;
        }
    }
    else if (c.p1 == 2 || c.p2 == 2) {
        
        if (c.p1 == 2) {
            struct reb_orbit o = reb_tools_particle_to_orbit(r->G, particles[c.p2], primary);

            FILE* ofae = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_ae_particle2.txt","a+");        // open file for collision output
            fprintf(ofae, "%e\t", t);
            fprintf(ofae, "%d\t", particles[c.p2].hash);                    // time, hash
            fprintf(ofae, "%e %e %e\t", o.a, o.e, o.inc);    // relative velocity
            fprintf(ofae, "\n");
            fclose(ofae);

            double vx_tp = particles[c.p2].vx;
            double vy_tp = particles[c.p2].vy;
            double vz_tp = particles[c.p2].vz;

            double vx_p = particles[c.p1].vx;
            double vy_p = particles[c.p1].vy;
            double vz_p = particles[c.p1].vz;

            double rel_vel = pow(pow(vx_tp-vx_p, 2.) + pow(vy_tp-vy_p, 2.) + pow(vz_tp-vz_p, 2.), 1./2.);
            double tp_vel = pow(pow(vx_tp, 2.) + pow(vy_tp, 2.) + pow(vz_tp, 2.), 1./2.);
            double plan_vel = pow(pow(vx_p, 2.) + pow(vy_p, 2.) + pow(vz_p, 2.), 1./2.);

            FILE* of = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_velocities_particle2.txt","a+");        // open file for collision output
            fprintf(of, "%e\t", t);                    // time
            fprintf(of, "%e %e %e\t", rel_vel, tp_vel,plan_vel);    // relative velocity
            fprintf(of, "\n");
            fclose(of);                        // close file

            return 2;
        }
        else if (c.p2 == 2) {
            struct reb_orbit o = reb_tools_particle_to_orbit(r->G, particles[c.p1], primary);

            FILE* ofae = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_ae_particle2.txt","a+");        // open file for collision output
            fprintf(ofae, "%e\t", t);
            fprintf(ofae, "%d\t", particles[c.p1].hash);                    // time, hash
            fprintf(ofae, "%e %e %e\t", o.a, o.e, o.inc);    // relative velocity
            fprintf(ofae, "\n");
            fclose(ofae);

            double vx_tp = particles[c.p1].vx;
            double vy_tp = particles[c.p1].vy;
            double vz_tp = particles[c.p1].vz;

            double vx_p = particles[c.p2].vx;
            double vy_p = particles[c.p2].vy;
            double vz_p = particles[c.p2].vz;

            double rel_vel = pow(pow(vx_tp-vx_p, 2.) + pow(vy_tp-vy_p, 2.) + pow(vz_tp-vz_p, 2.), 1./2.);
            double tp_vel = pow(pow(vx_tp, 2.) + pow(vy_tp, 2.) + pow(vz_tp, 2.), 1./2.);
            double plan_vel = pow(pow(vx_p, 2.) + pow(vy_p, 2.) + pow(vz_p, 2.), 1./2.);

            FILE* of = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_velocities_particle2.txt","a+");        // open file for collision output
            fprintf(of, "%e\t", t);                    // time
            fprintf(of, "%e %e %e\t", rel_vel, tp_vel, plan_vel);    // relative velocity
            fprintf(of, "\n");
            fclose(of);                        // close file

            return 1;
        }
    }

    else if (c.p1 == 3 || c.p2 == 3) {
        
        if (c.p1 == 3) {
            struct reb_orbit o = reb_tools_particle_to_orbit(r->G, particles[c.p2], primary);

            FILE* ofae = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_ae_particle1.txt","a+");        // open file for collision output
            fprintf(ofae, "%e\t", t);
            fprintf(ofae, "%d\t", particles[c.p2].hash);                    // time, hash
            fprintf(ofae, "%e %e %e\t", o.a, o.e, o.inc);    // relative velocity
            fprintf(ofae, "\n");
            fclose(ofae);

            double vx_tp = particles[c.p2].vx;
            double vy_tp = particles[c.p2].vy;
            double vz_tp = particles[c.p2].vz;

            double vx_p = particles[c.p1].vx;
            double vy_p = particles[c.p1].vy;
            double vz_p = particles[c.p1].vz;

            double rel_vel = pow(pow(vx_tp-vx_p, 2.) + pow(vy_tp-vy_p, 2.) + pow(vz_tp-vz_p, 2.), 1./2.);
            double tp_vel = pow(pow(vx_tp, 2.) + pow(vy_tp, 2.) + pow(vz_tp, 2.), 1./2.);
            double plan_vel = pow(pow(vx_p, 2.) + pow(vy_p, 2.) + pow(vz_p, 2.), 1./2.);

            FILE* of = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_velocities_particle1.txt","a+");        // open file for collision output
            fprintf(of, "%e\t", t);                    // time
            fprintf(of, "%e %e %e\t", rel_vel, tp_vel,plan_vel);    // relative velocity
            fprintf(of, "\n");
            fclose(of);                        // close file

            return 2;
        }
        else if (c.p2 == 3) {
            struct reb_orbit o = reb_tools_particle_to_orbit(r->G, particles[c.p1], primary);

            FILE* ofae = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_ae_particle1.txt","a+");        // open file for collision output
            fprintf(ofae, "%e\t", t);
            fprintf(ofae, "%d\t", particles[c.p1].hash);                    // time, hash
            fprintf(ofae, "%e %e %e\t", o.a, o.e, o.inc);    // relative velocity
            fprintf(ofae, "\n");
            fclose(ofae);

            double vx_tp = particles[c.p1].vx;
            double vy_tp = particles[c.p1].vy;
            double vz_tp = particles[c.p1].vz;

            double vx_p = particles[c.p2].vx;
            double vy_p = particles[c.p2].vy;
            double vz_p = particles[c.p2].vz;

            double rel_vel = pow(pow(vx_tp-vx_p, 2.) + pow(vy_tp-vy_p, 2.) + pow(vz_tp-vz_p, 2.), 1./2.);
            double tp_vel = pow(pow(vx_tp, 2.) + pow(vy_tp, 2.) + pow(vz_tp, 2.), 1./2.);
            double plan_vel = pow(pow(vx_p, 2.) + pow(vy_p, 2.) + pow(vz_p, 2.), 1./2.);

            FILE* of = fopen("/data/rja92/rebound_outputs/stellar_type_N_pl_experiment/Kdwarf_delta30/collision_velocities_particle1.txt","a+");        // open file for collision output
            fprintf(of, "%e\t", t);                    // time
            fprintf(of, "%e %e %e\t", rel_vel, tp_vel, plan_vel);    // relative velocity
            fprintf(of, "\n");
            fclose(of);                        // close file

            return 1;
        }
    }


}

double E0;
double counter;
void heartbeat(struct reb_simulation* r){
    if (reb_output_check(r, 1.*r->dt)){
        // reb_output_timing(r, 0);
        double E = reb_tools_energy(r);
        double relE = fabs((E-E0)/E0);

        //get orbital elements
        struct reb_particle p = r->particles[1];
        struct reb_particle star = r->particles[0];
        struct reb_orbit o = reb_tools_particle_to_orbit(r->G,p,star);

        printf("a2=%f,dE=%e,N=%d,t=%e,dt=%e\n",o.a,relE,r->N, r->t, r->dt);
    }

    if (reb_output_check(r, 1000.*r->dt)){
        int keepSorted = 0;
        
        double a_p3 = 3.009;
        double m_p3 = 3.00273e-6;

        struct reb_particle* particles = r->particles;
        struct reb_particle primary = r->particles[0];
        
        // printf("Removing particles on hyperbolic orbits.");

        for (int i=r->N_active;i<r->N;i++){
            struct reb_orbit o = reb_tools_particle_to_orbit(r->G, particles[i], primary);

            if(o.a * (1 - o.e) > 10*a_p3){
                reb_remove(r, i, keepSorted);

                double amin = a_p3 * (1. + .2 * 2. * pow(m_p3/1., 2./7.)), amax = a_p3 * (1. + 1. * 2. * pow(m_p3/1., 2./7.));   //planet at inner edge of disk

                double a = reb_random_uniform(r, amin, amax);
                double T = 2.9;
                double e = pow(1 - (a_p3/a)*pow(T/2. - a_p3 / (2. * a), 2.), 1./2.);
                double omega = reb_random_uniform(r, 0., 2.*M_PI);
                double f = reb_random_uniform(r, 0., 2.*M_PI);
                struct reb_particle p = reb_tools_orbit_to_particle(r->G,r->particles[0],0.,a,e,0.,0.,omega,f);
                p.r         = 0.;
                p.hash = i;
                reb_add(r, p);
            }
        }
    }

    if (reb_output_check(r, 100000000.*r->dt)){
        int keepSorted = 0;
        
        double a_p3 = 3.009;
        double m_p3 = 3.00273e-6;

        struct reb_particle* particles = r->particles;
        struct reb_particle primary = r->particles[0];

        for (int i=r->N_active;i<r->N;i++){
            struct reb_orbit o = reb_tools_particle_to_orbit(r->G, particles[i], primary);

            if ((double)rand() / (double)RAND_MAX < 0.1){
                reb_remove(r, i, keepSorted);

                double amin = a_p3 * (1. + .2 * 2. * pow(m_p3/1., 2./7.)), amax = a_p3 * (1. + 1. * 2. * pow(m_p3/1., 2./7.));   //planet at inner edge of disk

                double a = reb_random_uniform(r, amin, amax);
                double T = 2.9;
                double e = pow(1 - (a_p3/a)*pow(T/2. - a_p3 / (2. * a), 2.), 1./2.);
                double omega = reb_random_uniform(r, 0., 2.*M_PI);
                double f = reb_random_uniform(r, 0., 2.*M_PI);
                struct reb_particle p = reb_tools_orbit_to_particle(r->G,r->particles[0],0.,a,e,0.,0.,omega,f);
                p.r         = 0.;
                p.hash = i;
                reb_add(r, p);
            }
        }

        while (r->N < 506){
            counter += 1;

            double amin = a_p3 * (1. + .2 * 2. * pow(m_p3/1., 2./7.)), amax = a_p3 * (1. + 1. * 2. * pow(m_p3/1., 2./7.));   //planet at inner edge of disk

            double a = reb_random_uniform(r, amin, amax);
            double T = 2.9;
            double e = pow(1 - (a_p3/a)*pow(T/2. - a_p3 / (2. * a), 2.), 1./2.);
            double omega = reb_random_uniform(r, 0., 2.*M_PI);
            double f = reb_random_uniform(r, 0., 2.*M_PI);
            struct reb_particle p = reb_tools_orbit_to_particle(r->G,r->particles[0],0.,a,e,0.,0.,omega,f);
            p.r         = 0.;
            p.hash = counter;
            reb_add(r, p);
        }
    }
}

int main(int argc, char* argv[]){
    struct reb_simulation* r = reb_create_simulation();

    r->G = 1;
    r->integrator    = REB_INTEGRATOR_MERCURIUS;
    r->ri_mercurius.hillfac = 5;
    r->heartbeat    = heartbeat;

    r->testparticle_type = 0;

    r->boundary = REB_BOUNDARY_OPEN;
    reb_configure_box(r, 1000, 1, 1, 1);

    // Collisions
    r->collision = REB_COLLISION_DIRECT;
    r->collision_resolve = collision_record_only;
    r->track_energy_offset = 1;

    struct reb_particle star = {0};
    star.m = 1.;
    star.r = 1. * 0.00465047;
    reb_add(r, star);

    double m_p3 = 3.00273e-6;
    double a_p3 = 3.009;
    {
        double a=a_p3, m=m_p3, e=0, inc=reb_random_normal(r, 0.);
        struct reb_particle planet = {0};
        planet = reb_tools_orbit_to_particle(r->G, star, m, a, e, inc, 0, 0, 0);
        planet.r = 4.26352e-5;
        reb_add(r, planet);
    }

    double m_p2 = 3.00273e-6;
    double a_p2 = 2.052;
    {
        double a=a_p2, m=m_p2, e=0, inc=reb_random_normal(r, 0.);
        struct reb_particle planet = {0};
        planet = reb_tools_orbit_to_particle(r->G, star, m, a, e, inc, 0, 0, 0);
        planet.r = 4.26352e-5;
        reb_add(r, planet);
    }

    double m_p1 = 3.00273e-6;
    double a_p1 = 1.4;
    {
        double a=a_p1, m=m_p1, e=0, inc=reb_random_normal(r, 0.);
        struct reb_particle planet = {0};
        planet = reb_tools_orbit_to_particle(r->G, star, m, a, e, inc, 0, 0, 0);
        planet.r = 4.26352e-5;
        reb_add(r, planet);
    }

    r->N_active = r->N;
    r->dt = 1.*pow(a_p1, 1.5)/50;

    int N_planetesimals = 500;
    double amin = a_p3 * (1. + .2 * 2. * pow(m_p3/1., 2./7.)), amax = a_p3 * (1. + 1. * 2. * pow(m_p3/1., 2./7.));   //planet at inner edge of disk

    // Test Particles
    for (int i=r->N_active;i<r->N_active + N_planetesimals;i++){
        double a = reb_random_uniform(r, amin, amax);
        double T = 2.9;
        double e = pow(1 - (a_p3/a)*pow(T/2. - a_p3 / (2. * a), 2.), 1./2.);
        double omega = reb_random_uniform(r, 0., 2.*M_PI);
        double f = reb_random_uniform(r, 0., 2.*M_PI);
        struct reb_particle p = reb_tools_orbit_to_particle(r->G,r->particles[0],0.,a,e,0.,0.,omega,f);
        p.r         = 0.;
        p.hash = i;
        reb_add(r, p);
    }

    reb_move_to_com(r);                // This makes sure the planetary systems stays within the computational domain and doesn't drift.
    E0 = reb_tools_energy(r);
    counter = r->N_active + N_planetesimals;

    reb_integrate(r, INFINITY);

    printf("\nFinal time: %f\n", r->t);
}