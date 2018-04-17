import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

#_________________________Problem 1_________________________
print("Problem 1")
print("")
# create and cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)

simOutputs_no = cohort.simulate()

SupportMarkov.print_outcomes(simOutputs_no, 'No treatment:')

cohort = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs_ac = cohort.simulate()

SupportMarkov.print_outcomes(simOutputs_ac, 'Treatment:')
print("")

#_________________________Problem 2_________________________
print("Problem 2")
print("")
SupportMarkov.print_comparative_outcomes(simOutputs_no, simOutputs_ac)
print("")

#_________________________Problem 3_________________________
print("Problem 3")
print("")
SupportMarkov.report_CEA_CBA(simOutputs_ac, simOutputs_no)
print("See Output & CE Table")
print("")

#_________________________Problem 3_________________________
print("Problem 4")
print("")
print("See Problem 3 for monetary curve ")
print("I would recommend adopting this anticoagulation drug if the level of"
      " willingness-to-pay is ~$10,000")