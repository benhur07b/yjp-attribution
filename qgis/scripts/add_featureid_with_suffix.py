from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingException,
                       QgsProcessingContext,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterString,
                       QgsProcessingOutputNumber,
                       QgsField,
                       QgsFeature,
                       QgsProject)
from qgis import processing
import numpy as np

class AddFeatureIDAlgorithm(QgsProcessingAlgorithm):

    def name(self):
        return 'addfeatureidwithsuffix'


    def displayName(self):
        return 'Add Feature ID with Suffix'

    def createInstance(self):
        return AddFeatureIDAlgorithm()
        
    def group(self):
        return 'YJP_Attribution'

    def groupId(self):
        return 'yjpattribution'

    def shortHelpString(self):
        return 'Add unique feature ID with a specified suffix to each feature in the layer. A "feature_id" field is created and each feature has a unique value of [Feature ID Suffix]_[num].'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('INPUT', 'Input Layer', types=[QgsProcessing.TypeVectorAnyGeometry]))
        self.addParameter(QgsProcessingParameterString('FEATURE_ID_SUFFIX', 'Feature ID Suffix', defaultValue=''))
        self.addOutput(QgsProcessingOutputNumber('NUMBEROFFEATURES', 'Number of features processed'))

    def flags(self):
        return super().flags() | QgsProcessingAlgorithm.FlagNoThreading

    def processAlgorithm(self, parameters, context, feedback):
        layer = self.parameterAsVectorLayer(parameters, 'INPUT', context)
        feature_id_suffix = self.parameterAsString(parameters, 'FEATURE_ID_SUFFIX', context)

        if layer is None:
            raise QgsProcessingException('Input layer not found')

        # Enable editing mode
        layer.startEditing()

        # Check if "feature_id" field exists, if not, create it
        if 'feature_id' not in [field.name() for field in layer.fields()]:
            new_field = QgsField("feature_id", QVariant.String)
            layer.addAttribute(new_field)
            layer.updateFields()

        # Get the index of the "feature_id" field
        feature_id_idx = layer.fields().indexFromName("feature_id")
        
        # Get number of features
        numfeatures = layer.featureCount()

        # Iterate over features in the layer
        for i, feature in enumerate(layer.getFeatures()):
            # Generate the feature ID with the specified suffix and 7-digit number
            new_feature_id = f"{feature_id_suffix}_{i:07d}"
            # Set the new feature ID
            feature.setAttribute(feature_id_idx, new_feature_id)
            # Update the feature in the layer
            layer.updateFeature(feature)

        # Commit changes to the layer
        layer.commitChanges()

        if feedback.isCanceled():
            return {}
        
        feedback.pushInfo(f"{numfeatures} features updated with new feature ID in the {layer.name()} layer.")
        
        return {'NUMBEROFFEATURES': numfeatures}