# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsProcessing,
    QgsFeatureSink,
    QgsProcessingException,
    QgsProcessingAlgorithm,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterBoolean,
    QgsProcessingParameterFeatureSink,
)
from qgis import processing


class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = "INPUT"
    OUTPUT = "OUTPUT"

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate("Processing", string)

    def createInstance(self):
        return ExampleProcessingAlgorithm()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return "myscript"

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr("Build2Vec 2.0")

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr("Example scripts")

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return "examplescripts"

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """

        desc = """ Build2vec is the building representation in vector space.
        Select spaces, nodes, Buffer elements (wall buffer, door buffer, stairlanding buffer, furniture buffer and so on. 
        then the algorithm will create a graph representation of the floor plan"""
        return self.tr(desc)

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT, self.tr("Nodes"), [QgsProcessing.TypeVectorPoint]
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "SPACES", "SAPCES", [QgsProcessing.TypeVectorPolygon]
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "WALLBUFFER", " WALL BUFFER", [QgsProcessing.TypeVectorAnyGeometry]
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "DOORBUFFER", "DOOR BUFFERS", [QgsProcessing.TypeVectorAnyGeometry]
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "CURTAINWALLBUFFER",
                "CURTAINWALLS BUFFER",
                [QgsProcessing.TypeVectorAnyGeometry],
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "HANDRAILBUFFER",
                "HANDRAILS BUFFER",
                [QgsProcessing.TypeVectorAnyGeometry],
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "FURNITUREBUFFER",
                "FURNITURE BUFFER",
                [QgsProcessing.TypeVectorAnyGeometry],
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "FURNITURELINESBUFFER",
                "FURNITURE LINES BUFFER",
                [QgsProcessing.TypeVectorAnyGeometry],
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "STAIRLANDING",
                "STAIR LANDING BUFFER",
                [QgsProcessing.TypeVectorAnyGeometry],
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "FANBUFFER",
                "FAN BUFFER",
                [QgsProcessing.TypeVectorAnyGeometry],
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                "ACBUFFER",
                "AC BUFFER",
                [QgsProcessing.TypeVectorAnyGeometry],
            )
        )

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.OUTPUT, self.tr("Output layer"))
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        space_node = "space\tcell\tspaceName\n"
        wall_node = "wall\tcell\n"
        door_node = "door\tcell\n"
        curtain_wall_node = "curtainWall\tcell\n"
        handrail_node = "handrail\tcell\n"
        furniture_node = "furniture\tcell\n"
        furniturelines_node = "furniture\tcell\n"
        stair_landing_node = "stairLanding\tcell\n"
        fan_node = "fan\tcell\n"
        ac_node = "ac\tcell\n"
        log = ""

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        source = self.parameterAsSource(parameters, self.INPUT, context)

        spaces = self.parameterAsSource(parameters, "SPACES", context)

        wallBuffer = self.parameterAsSource(parameters, "WALLBUFFER", context)

        doorBuffer = self.parameterAsSource(parameters, "DOORBUFFER", context)

        curtainWallBuffer = self.parameterAsSource(
            parameters, "CURTAINWALLBUFFER", context
        )

        handrailBuffer = self.parameterAsSource(parameters, "HANDRAILBUFFER", context)

        furnitureBuffer = self.parameterAsSource(parameters, "FURNITUREBUFFER", context)

        furniturelinesBuffer = self.parameterAsSource(
            parameters, "FURNITURELINESBUFFER", context
        )

        stairLandingBuffer = self.parameterAsSource(parameters, "STAIRLANDING", context)

        fanBuffer = self.parameterAsSource(parameters, "FANBUFFER", context)
        acBuffer = self.parameterAsSource(parameters, "ACBUFFER", context)

        # If source was not found, throw an exception to indicate that the algorithm
        # encountered a fatal error. The exception text can be any string, but in this
        # case we use the pre-built invalidSourceError method to return a standard
        # helper text for when a source cannot be evaluated
        if source is None:
            raise QgsProcessingException(
                self.invalidSourceError(parameters, self.INPUT)
            )

        (sink, dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            source.fields(),
            source.wkbType(),
            source.sourceCrs(),
        )

        # Send some information to the user
        feedback.pushInfo("CRS is {}".format(source.sourceCrs().authid()))

        # If sink was not created, throw an exception to indicate that the algorithm
        # encountered a fatal error. The exception text can be any string, but in this
        # case we use the pre-built invalidSinkError method to return a standard
        # helper text for when a sink cannot be evaluated
        if sink is None:
            raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT))

        # Compute the number of steps to display within the progress bar and
        # get features from source
        total = 100.0 / source.featureCount() * 1000 if source.featureCount() else 0

        spaceFeats = spaces.getFeatures()
        wallBufferFeats = wallBuffer.getFeatures()
        doorBufferFeats = doorBuffer.getFeatures()
        curtainWallBufferFeats = curtainWallBuffer.getFeatures()
        handrailBufferFeats = handrailBuffer.getFeatures()
        furnitureBufferFeats = furnitureBuffer.getFeatures()
        furniturelinesBufferFeats = furniturelinesBuffer.getFeatures()
        stairLandingBufferFeats = stairLandingBuffer.getFeatures()
        fanBufferFeats = fanBuffer.getFeatures()
        acBufferFeats = acBuffer.getFeatures()

        allFeats = [
            wallBufferFeats,
            doorBufferFeats,
            curtainWallBufferFeats,
            handrailBufferFeats,
            furnitureBufferFeats,
            furniturelinesBufferFeats,
            stairLandingBufferFeats,
            fanBufferFeats,
            acBufferFeats,
        ]
        allFeatTexts = [
            wall_node,
            door_node,
            curtain_wall_node,
            handrail_node,
            furniture_node,
            furniturelines_node,
            stair_landing_node,
            fan_node,
            ac_node,
        ]

        tsvFileNames = [
            "wall_node",
            "door_node",
            "curtain_wall_node",
            "handrail_node",
            "furniture_node",
            "furniturelines_node",
            "stair_landing_node",
            "fan_node",
            "ac_node",
        ]

        for i in range(len(allFeats)):
            for feat in allFeats[i]:
                nodeFeats = source.getFeatures()
                geom = feat.geometry()

                for j, feature in enumerate(nodeFeats):
                    nodegeom = feature.geometry()
                    if geom.contains(nodegeom):

                        allFeatTexts[i] += feat["GUID"] + "\t" + feature["GUID"] + "\n"
            with open(
                "/Users/mahmoud/Documents/qgis/sde4/TSV_GRAPH/LEVEL3/"
                + tsvFileNames[i]
                + ".tsv",
                "w",
            ) as f:
                f.write(allFeatTexts[i])

        # for sFeat in spaceFeats:
        #     nodeFeats = source.getFeatures()

        #     spacegeom = sFeat.geometry()
        #     for i, feature in enumerate(nodeFeats):
        #         geom = feature.geometry()
        #         if spacegeom.contains(geom):
        #             space_node += (
        #                 sFeat["GUID"]
        #                 + "\t"
        #                 + feature["GUID"]
        #                 + "\t"
        #                 + sFeat["NAME"]
        #                 + "\n"
        #             )

        if False:
            buffered_layer = processing.run(
                "native:buffer",
                {
                    "INPUT": dest_id,
                    "DISTANCE": 1.5,
                    "SEGMENTS": 5,
                    "END_CAP_STYLE": 0,
                    "JOIN_STYLE": 0,
                    "MITER_LIMIT": 2,
                    "DISSOLVE": False,
                    "OUTPUT": "memory:",
                },
                context=context,
                feedback=feedback,
            )["OUTPUT"]

        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        return {self.OUTPUT: dest_id, "names": log}
