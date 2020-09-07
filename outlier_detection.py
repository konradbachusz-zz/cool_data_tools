#Interquartile range outlier detection function
def outlier_detection(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)

    #Calculate the interquartile range
    IQR = Q3 - Q1
    outlier_upper_threshold=Q3 + 1.5 * IQR
    outlier_lower_threshold=Q1 - 1.5 * IQR
    
    #Values outside this range are outliers
    outlier_thresholds=[outlier_lower_threshold,outlier_upper_threshold]
    return outlier_thresholds