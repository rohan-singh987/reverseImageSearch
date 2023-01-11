# Reverse Image Search && Recommendation System

- Deep Learning —> CNN
- Transfer Learning (Technique to use pre-trained model) —> we are going to use the ResNet model 
- ResNET is model trained on ImageNET -> It will work as a Feature Extractor for model

## Plan of Attack

1. Import model  (ResNET from Keras)
		    we are going to use the already build model ResNet because we cannot achieve the accuracy that ResNet already have
2. Extract Features
		    For every image, our ResNet model will provide 2048 features. 
3. Export Features
		    We already have [44k, 2048] dataSet, we will save new image data i.e. [1,2048]
4. Generate Recommendations	
		    Now we will check the euclidean distance between new image [1, 2048] to [44k, 2048]  using KNN model.