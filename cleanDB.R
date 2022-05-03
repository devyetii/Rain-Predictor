rm(list=ls())

setwd("A:\\CMP last year\\6) Big Data\\project\\Big-Data-and-Analytics")

Dataset <- read.csv("north.csv",header = TRUE)

Dataset<- subset(Dataset, Dataset$ATMOSPHERIC.PRESSURE.AT.STATION.LEVEL..TIME..mB. != "-9999")
Dataset<- subset(Dataset, Dataset$TOTAL.PRECIPITATION..SCHEDULE..mm. != "-9999")
Dataset<- subset(Dataset, Dataset$MAX..ATMOSPHERIC.PRESSURE.IN.THE.PREVIOUS.TIME...AUT...mB. != "-9999")
Dataset<- subset(Dataset, Dataset$ATMOSPHERIC.PRESSURE.MIN..IN.THE.EARLY.TIME...AUT...mB. != "-9999")
Dataset<- subset(Dataset, Dataset$`GLOBAL.RADIATION..Kj...mÂ².` != "-9999")
Dataset<- subset(Dataset, Dataset$AIR.TEMPERATURE...DRY.BULB..TIME..Â.C. != "-9999")
Dataset<- subset(Dataset, Dataset$DEW.POINT.TEMPERATURE..Â.C. != "-9999")
Dataset<- subset(Dataset, Dataset$MINIMUM.TEMPERATURE.BEFORE...AUT...Â...C. != "-9999")
Dataset<- subset(Dataset, Dataset$TEMPERATURA.MÃ.NIMA.NA.HORA.ANT...AUT...Â.C. != "-9999")
Dataset<- subset(Dataset, Dataset$DEW.TEMPERATURE.MAX..IN.THE.EARLY.TIME...OUT...Â.C. != "-9999")
Dataset<- subset(Dataset, Dataset$TEMPERATURE.DEW.ME..IN.THE.EARLY.TIME...OUT...Â.C. != "-9999")
Dataset<- subset(Dataset, Dataset$REL..HUMIDITY.MAX..IN.THE.EARLY.TIME...AUT..... != "-9999")
Dataset<- subset(Dataset, Dataset$REL..HUMIDITY.MIN.IN.THE.EARLY.TIME...AUT..... != "-9999")
Dataset<- subset(Dataset, Dataset$RELATIVE.AIR.HUMIDITY..HOURS.... != "-9999")
Dataset<- subset(Dataset, Dataset$WIND..TIME.DIRECTION..gr...Â...gr.. != "-9999")
Dataset<- subset(Dataset, Dataset$WIND..MAXIMUM.GUNS..m.s. != "-9999")
Dataset<- subset(Dataset, Dataset$WIND..HOUR.SPEED..m.s. != "-9999")


write.csv(Dataset, file = "north_clean.csv")