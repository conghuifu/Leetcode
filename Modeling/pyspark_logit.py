from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler

def predict_cancellations(user_interaction_df):
    assembler = VectorAssembler(
        inputCols = ['month_interaction_count', 'week_interaction_count', 'day_interaction_count'], outputCol = 'features'
    )
    
    feature_df = assembler.transform(user_interaction_df)
    feature_df = feature_df.withColumn('label', feature_df['cancelled_within_week'])

    lr_model = LogisticRegression(maxIter=10, threshold=0.6, elasticNetParam=1, regParam=0.1)
    trained_lr_model = lr_model.fit(feature_df)

    predictions_df = trained_lr_model.transform(feature_df)
    predictions_df = predictions_df.select(['user_id', 'rawPrediction', 'probability', 'prediction'])

    return predictions_df