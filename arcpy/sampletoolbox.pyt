import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Sample Toolbox"
        self.alias = "sampletoolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Sample Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""

        # First parameter
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

         # Second parameter
        param1 = arcpy.Parameter(
            displayName="Output Features",
            name="out_features",
            datatype="GPFeatureLayer",
            parameterType="Derived",
            direction="Output")

        param1.parameterDependencies = [param0.name]
        param1.schema.clone = True

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        input = parameters[0].valueAsText
            
        # If the input has no features, add an error message, and raise
        #  an arcpy.ExecuteError
        count = int(arcpy.GetCount_management(input)[0])
        if count == 0:
            messages.addErrorMessage("{0} has no features.".format(input))
            raise arcpy.ExecuteError
        else:
            messages.addMessage("{0} has {1} features.".format(input, count))

        return