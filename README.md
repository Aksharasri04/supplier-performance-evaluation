# Geospatial Analytics for Supplier Performance Evaluation.

## Watch my Video Walkthrough
  https://www.youtube.com/watch?v=-vojmnTcsm8
  
## Website 
  https://sites.google.com/view/aksharalakshmipathy/home
  
## Motivation 
Use geospatial analytics and machine learning to evaluate supplier performance and delivery risk so businesses can choose reliable suppliers, predict delays, and optimize shipment decisions (mode, routes, costs). My research questions cover risk clustering, distance vs. delay, shipment mode effects, Incoterms, order size, and regional patterns.

## What I Built 
- Data sources: Supplier data (Kaggle) + geocoding via OpenStreetMap API and road distance via OSRM; created lat/lon for manufacturing & warehouse.
- Feature engineering & cleaning: Parsed location fields, standardized datetimes, engineered Delay (actual − scheduled), converted Distance to miles, and produced a clean dataset 
- EDA & geo-viz: Shipment mode mix (Air, Truck, Ocean, Air Charter), correlation heatmaps, distance & delay distributions, and world-map scatter of manufacturing vs. warehouse locations 
- Unsupervised learning: PCA and clustering (K-Means, Hierarchical, DBSCAN). 
- Association Rule Mining: Derived shipment/vendor/country/Incoterm patterns with minimum lift  and confidence.
- Supervised models: Logistic Regression, Naive Bayes variants, Decision Trees, SVM (linear/poly/RBF), and Ensembles (AdaBoost, Random Forest, Bagging).

## Result 
- Built predictive models where SVM (RBF) reached ~73% accuracy and AdaBoost ensemble ~72%, outperforming baseline models.
- Discovered key supply chain insights — Air shipments dominated (~58.7%), and association rule mining revealed strong links between shipment mode, Incoterms, and vendor reliability.
- Delivered a complete geo-ML pipeline integrating mapping (OpenStreetMap, OSRM), unsupervised learning, and supervised ML for supplier performance evaluation and risk analysis.
