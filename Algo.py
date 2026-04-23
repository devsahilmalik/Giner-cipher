import json

master_table = "q+0¥4fCpn=?!>G3(Thb™dy'~U\"©r€j@k¢]N$A9i-R1% ∆O,π`F#8KX*J√M2s5÷Ie_mu&S°×.:•lzx✓§6w)DY7{₹[Lgo®Ht;c\\W<ZQv/PE|aB^}V"
with open("hash_table.json", "r") as f:
  hash_table = json.load(f)
with open("super_table.json", "r") as f:
  super_table = json.load(f)

#function to unjoin chars and make numbers
def zigzag(key):
  tables = []
  num_index = []
  for k in key:
    val = master_table.find(k)
    table = "table" + str(val)
    tables.append(table)
  count = 0
  for k in key:
    val = super_table[tables[count]].find(k)
    num_index.append(val)
    count += 1
  return start_hash(num_index, tables)
  
def start_hash(num, tables):
  hash1 = ""
  
  count = 0
  for i in num:
    val1 = str(i)
    for j in val1:
      n = int(j)
      val = hash_table[tables[count]][n]
      hash1 += val
    count += 1
      
      
  return length_checker(hash1)
  
      
def length_checker(hash):
  hash1 = hash
  while len(hash1) < 111:
    hash1 = zigzag(hash1)
  
  return right_length(hash1)
def right_length(hash):
  hash1 = ""
  for i in hash:
    if len(hash1) == 111:
      break
    else:
      hash1 += i
  return hash1


__name__=="__main__"
  