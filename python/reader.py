def trainortest():
    ''' The value will be returned as dataset,attribute_size,datasize'''
    #enter filename.csv
    f_name=input('Enter file name ')
    load=open(f_name,'r')
    loaded=load.read()
    loaded=loaded.split('\n')
    #removing metarow
    metad=loaded.pop(0)
    acn=len(loaded[0].split(','))
    #dataset count
    dcn=int(len(loaded))
    return [loaded,acn,dcn,metad]
