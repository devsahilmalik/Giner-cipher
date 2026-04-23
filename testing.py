import random
import json
import Algo
trace_table = "@#₹_&-+()/*':;!?`~|•√π×÷§∆\\{°{}°^¢$€¥%©®™✓[]><"

conditional1 = "$=:y√3m§Xv5oL\"I]÷%©G<rQC#Vk;RAgKaF}2'[zwY)U™M∆N•Je¢B\\fπp76^Dlq®T9O¥?4×uP_€|HEW >~b₹x-`!S.°h1Z*+{j/(i✓n,&0sd@8tc"

conditional2 = "]h&Ne[~@^uzatcr\"`/9®sp5*GA§Q<∆;C2?E.0D-€Z!4F°•Riw¥1X™Kπ3{T×J₹%Vyq)\\7n=÷#¢(✓xL'j©SH} UWIl>,fd_$:B6√oM|PObmvYk+g8"
master_table = "q+0¥4fCpn=?!>G3(Thb™dy'~U\"©r€j@k¢]N$A9i-R1% ∆O,π`F#8KX*J√M2s5÷Ie_mu&S°×.:•lzx✓§6w)DY7{₹[Lgo®Ht;c\\W<ZQv/PE|aB^}V"
with open("super_table.json", "r") as f:
    super_table = json.load(f)
with open("final_table.json", "r") as f:
  final_table = json.load(f)
  unknown_tables = {}
def dynamic_tables(text, key, con):
  table = ""
  tables = []
  table_look = []
  for i in key:
    val = master_table.find(i)
    if val < 56:
      val1 = conditional1.find(i)
      table_look.append(val1)
      tables.append("table" + str(val1))
    else:
      val1 = conditional2.find(i)
      table_look.append(val1)
      tables.append("table" + str(val1))
  count = 0
  while len(unknown_tables) < 111:
    for i in tables:
      val = super_table[i].find(key[count])
      for j in super_table[i][val:]:
        if j in table:
          pass
        else:
          table += j
      
    table1 = "table" + str(count)
    unknown_tables[table1] = table
    table = ""
    count += 1
  if con == 1:
    return encryption(plain_text, key)
  else:
    return decryption(text, key)
  
def encryption(plain_text, key):
  cipher_text = ""
  preparation = ""
  tables = []
  for k in key:
    val = master_table.find(k)
    if val < 56:
      val1 = conditional1.find(k)
      tables.append("table" + str(val1))
    else:
      val1 = conditional2.find(k)
      tables.append("table" + str(val1))
  count = 0
  count1 = 0
  for p in plain_text:
    val1 = master_table.find(p)
    val2 = unknown_tables[tables[count]].find(key[count])
    val3 = val1 ^ val2
    val4 = str(val3)
    for j in val4:
      val1 = int(j)
      val5 = final_table[tables[count1]][val1]
      preparation += val5
      count1 += 1
    val6 = random.choice(trace_table)
    cipher_text += preparation + val6
    preparation = ""
    count1 = 0
    count += 1
   
  print("Encrypted text Is below")
  print(".............................................")
  print("")
  print(cipher_text)
  print("")
  print(".............................................")

def decryption(cipher_text, key):
  plain_text = ""
  tables = []
  cipher_int = []
  cipher_split = []
  right_value = ""
  for k in key:
    val = master_table.find(k)
    if val < 56:
      val1 = conditional1.find(k)
      tables.append("table" + str(val1))
    else:
      val1 = conditional2.find(k)
      tables.append("table" + str(val1))
      
  for i in cipher_text:
    if i in trace_table:
      cipher_split.append(right_value)
      right_value = ""
    else:
      right_value += i
  right_value = ""
  count = 0
  count1 = 0
  for i in cipher_split:
    for j in i:
      val1 = final_table[tables[count]].find(j)
      right_value += str(val1)
      count += 1
    cipher_int.append(right_value)
    right_value = ""
    count = 0
  count = 0
  for i in cipher_int:
    val1 = int(i)
    val2 = unknown_tables[tables[count]].find(key[count])
    val3 = val1 ^ val2
    val4 = master_table[val3]
    plain_text += val4
    count += 1
  print("Decrypted text is below")  
  print(".............................................")
  print("")
  print(plain_text)
  print("")
  print(".............................................")
      
while True:
  print("1 For encryption")
  print("2 For decryption")
  print("3 For exit")
  user = input("Choose an option: ")
  if user == "3":
    break
  elif user == "1":
    plain_text = input("Enter plain text: ")
    key = input("Enter key: ")
    ke = Algo.zigzag(key)
    con = 1
    dynamic_tables(plain_text, ke, con)
  elif user == "2":
    cipher_text = input("Enter cipher text: ")
    key = input("Enter key: ")
    ke = Algo.zigzag(key)
    con = 2
    dynamic_tables(cipher_text, ke, con)