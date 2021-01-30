#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import chain

vocab = open('file1.txt').read().split("\n")
gold = open('file2.txt').read().split("\n")

"""vocab=['ketab khaneh','danesh gah']
gold=['ketab khaneh','dan esh gah']"""

tp=0
array1=[]
array2=[]
array3=[]
array4=[]
array5=[]
array6=[]
for i in range(len(vocab)):
        x  = sum(c.isspace() for c in vocab[i])
        z=sum(c.isspace() for c in gold[i])
        y=set(chain(*map(str.split, vocab))).intersection(chain(*map(str.split, gold)))
        tp=(len(y)+((len(vocab)*2)))-x
        array2.append(z+2)
        array3.append(x+2)
        
        array4.append(z+1)
        array5.append(x+1)
        
        if vocab[i]==gold[i]:
            array6.append(1)
        else:
            array6.append(0)
 
print("-----------------boundary evaluation---------------")
recall_boundary=tp/sum(array2)
print("recall of boundary=",tp,"/",sum(array2),"=",recall_boundary)

precision_boundary=tp/sum(array3)
print("precision of boundary=",tp,"/",sum(array3),"=",precision_boundary)

print("F-measure of boundary=",2*precision_boundary*recall_boundary/(recall_boundary+precision_boundary))

print("\n-----------------morpheme evaluation---------------")
recall_morpheme=len(y)/sum(array4)
print("recall of morpheme=",len(y),"/",sum(array4),"=",recall_morpheme)

precision_morpheme=len(y)/sum(array5)
print("recall of morpheme=",len(y),"/",sum(array5),"=",precision_morpheme)

print("F-measure of morpheme=",2*precision_morpheme*recall_morpheme/(recall_morpheme+precision_morpheme))

print("\n-----------------segmentation evaluation---------------")
recall_segmentation=sum(array6)/len(gold)
print("recall of morpheme=",sum(array6),"/",len(gold),"=",recall_segmentation)

precision_segmentation=sum(array6)/len(vocab)
print("recall of morpheme=",sum(array6),"/",len(vocab),"=",precision_segmentation)

print("F-measure of segmentation=",2*precision_segmentation*recall_segmentation/(recall_segmentation+precision_segmentation))

