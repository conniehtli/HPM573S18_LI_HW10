POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03


PSA_ON = False

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # Well
    [0,     0.0,    1.0,    0.0],   # Stroke
    [0,     0.25,   0.55,   0.2],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Dead
    ]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0,     # WELL
    5000,  # STROKE
    200,   # POST-STROKE
    0      # DEAD
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1.0,    # WELL
    0.8865, # STROKE
    0.9,    # POST-STROKE
    0.0     # DEAD
    ]

# annual drug costs
ANTICOAG_COST = 2000
NOTREAT_COST = 0


# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05