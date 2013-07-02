'''
Created on 2012-12-4

@author: SongYang
'''
from calcore.controllers.Dragon import Dragon
class PredictionModel_ForParamInDragon(object):
    '''
this class is used for model computation that parameters needed in Dragon output file
    '''
    def __init__(self , modelname=None ,para={},predict_results=None,molpath={}):
        self.predict_result = predict_results
        para = para or {}
        #start to compute model  results
        d = Dragon(smiles_str=para["smilestring"],
                molfile=para["filename"],molpath=molpath)
        d.mol2drs()
        self.predict_result["invalidnums"] = d.invalidnums
        modelname = modelname or []
        for name in modelname:
            self.models_computation(name, para ,d)
        print self.predict_result
        print "--------------------------------------------------"
#print the model results
    def models_computation(self, modelname, para ,instance_of_dragon):
                    {
         "logKOA" :  lambda para:self.logKOA(para ,instance_of_dragon),
         "logRP"  :  lambda para:self.logRP(para ,instance_of_dragon),
         "logKOF" :  lambda para:self.logKOF(para ,instance_of_dragon),
         
        }[modelname](para)
    def logKOA(self, para ,d):
        '''
        logKOA model computation
        '''
        abstract_value = d.extractparameter(["X1sol", "Mor13v", "HATS5v", "RDF035m","Mor15u" ,"RDF090m", "H-050", "nRCOOR", "R5v", "T(O..Cl)", "RCI","nRCOOR"])
        for smilenum in abstract_value.keys():
            if not self.predict_result.has_key(smilenum):
                self.predict_result[smilenum] = {}
            self.predict_result[smilenum]['logKOA'] = 0.509 + 0.986*float(abstract_value[smilenum]['X1sol'])-1.018*float(abstract_value[smilenum]['Mor13v'])+ \
            1.384*float(abstract_value[smilenum]['H-050'])-1.528*float(abstract_value[smilenum]['R5v'])-0.015*float(abstract_value[smilenum]['T(O..Cl)'])+ \
            0.043*float(abstract_value[smilenum]['HATS5v'])-0.026*float(abstract_value[smilenum]['RDF035m'])-0.197*float(abstract_value[smilenum]['RCI'])- \
            0.130*float(abstract_value[smilenum]['nRCOOR'])-0.077*float(abstract_value[smilenum]['Mor15u'])-0.077*float(abstract_value[smilenum]['RDF090m'])
    def logRP(self, para,d):
        '''
        logRP model computation
        '''
        abstract_value = d.extractparameter(["TDB05v", "Hypnotic-80"])
        for smilenum in abstract_value.keys():
            if not self.predict_result.has_key(smilenum):
                self.predict_result[smilenum] = {}
            self.predict_result[smilenum]['logRP'] = -11.5+16.6*float(abstract_value[smilenum]['TDB05v'])+1.81*float(abstract_value[smilenum]['Hypnotic-80'])
    def logKOF(self, para,d):
        '''
        logKOF model computation
        '''
        abstract_value=d.extractparameter(["Wap","WiA_Dt","SM1_B(p)","P_VSA_LogP_4","P_VSA_s_1","H_G/D","Mor07e","nROH","nR=CRX","O-057","CATS2D_05_Dn","B05[C-O]","MLOGP","ALOGP2","LLS_01"])
        for smilenum in abstract_value.keys():
            if not self.predict_result.has_key(smilenum):
                self.predict_result[smilenum]={}
            self.predict_result[smilenum]['logKOF']=-0.0000137*float(abstract_value[smilenum]['Wap'])+0.18*float(abstract_value[smilenum]['WiA_Dt'])+ \
            0.687*float(abstract_value[smilenum]['SM1_B(p)'])-0.008*float(abstract_value[smilenum]['P_VSA_LogP_4'])-0.034*float(abstract_value[smilenum]['P_VSA_s_1'])- \
            0.001*float(abstract_value[smilenum]['H_G/D'])-0.086*float(abstract_value[smilenum]['Mor07e'])-0.373*float(abstract_value[smilenum]['nROH'])+ \
            0.815*float(abstract_value[smilenum]['nR=CRX'])+0.279*float(abstract_value[smilenum]['O-057'])+0.975*float(abstract_value[smilenum]['CATS2D_05_Dn'])- \
            0.209*float(abstract_value[smilenum]['B05[C-O]'])+0.161*float(abstract_value[smilenum]['MLOGP'])+0.03*float(abstract_value[smilenum]['ALOGP2'])-0.983*float(abstract_value[smilenum]['LLS_01'])+0.619
            


MODEL_FOR_COMPUTAIONCLASS = {}
MODEL_FOR_COMPUTAIONCLASS["logKOA"] =  PredictionModel_ForParamInDragon
MODEL_FOR_COMPUTAIONCLASS["logRP"]  =  PredictionModel_ForParamInDragon
MODEL_FOR_COMPUTAIONCLASS["logKOF"] =  PredictionModel_ForParamInDragon
class PredictionModel(object):
    def __init__(self, modelnames=None, para={}, molpath={}):
        modelnames = modelnames or []
        predictionclass = {}
        self.predict_results={}
        #1:put all computation-needed prediction models name into predictionclass
        #the key of predictionclass is different computation models 
        #and the value is models'name list
        for modelname in modelnames:
            if not predictionclass.has_key(MODEL_FOR_COMPUTAIONCLASS[modelname]):
                predictionclass[MODEL_FOR_COMPUTAIONCLASS[modelname]] = []
            predictionclass[MODEL_FOR_COMPUTAIONCLASS[modelname]].append(modelname)
        #2:start to initiate different computation models 
        for prediction_model in predictionclass.keys():
            prediction_model(predictionclass[prediction_model],
                    para,self.predict_results,molpath)
'''            
para ={
    "smilestring":"c1ccccc1C(=O)c1cc(c(cc1O)OC)S(=O)(=O)O,c1(ccc(cc1)OC)/C=C/C(=O)OCCOCC",
    "filename"   :"",
    "cas"        :"",
       }  
pm = PredictionModel(["logKOA", "logRP"], para)
'''
