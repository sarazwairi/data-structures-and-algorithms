from data_structures.hashtable import HashTable
def hashmap_left_join(ht1,ht2):
  output=[]
  for item in ht1._buckets:
    if item:
      output1=[]
      node=item.head
      while node:
        key=item.head.value[0]
        value=item.head.value[1]
        output1+=[key,value]
        if ht2.contains(key):
            output1+=[ht2.get(key)]
        else:
            output1+=['Null']
        output+=[output1]
        node=node.next
  return output

if __name__=="__main__":
    ht1=HashTable()
    ht2=HashTable()
    ht1.add('sara','enamored')
    ht1.add('wrath','anger')
    ht1.add('diligent','employed')
    ht2.add('fond','averse')
    ht2.add('sama','delight')
    ht2.add('diligent','idle')
    print(hashmap_left_join(ht1,ht2))

