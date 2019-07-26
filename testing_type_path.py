#function_type = "T->U->T"
function_type = "T->U->B->A"
expression_type = "T->U->B"

application_type = ""

if function_type is not None:
    function_type_journey = function_type.split("->")
    if expression_type is not None:
        expression_type_journey = expression_type.split("->")
        application_type_journey = []

        if len(function_type_journey) > len(expression_type_journey):
            type_mismatch = False
            while len(expression_type_journey) > 0:
                if function_type_journey[0] != expression_type_journey[0]:
                    expression_type_journey = []
                    type_mismatch = True
                else:
                    del function_type_journey[0]
                    del expression_type_journey[0]
            if type_mismatch == False:
                application_type_journey = function_type_journey

            for i,journey_step in enumerate(application_type_journey):
                application_type = application_type + "->" + application_type_journey[i]

            application_type=application_type[2:]

if application_type == "":
    application_type = "None"

print("Application type = "+str(application_type))
