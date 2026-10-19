print ("FIFO Page Replacement")
pages = [1,2,3,4,5,1,2,3,1]
cap  = 3
frame = []
fault = 0
hit = 0

for page in pages:
    if page in frame:
        hit += 1
        print (page , "----->" , frame , "Hit")

    else:
        fault += 1

        if len (frame) < cap:
            frame.append (page)

        else:
            frame.pop(0)
            frame.append(page)

    print (page , "----->" , frame , "Fault")

print ("Total Hits = " , hit)
print ("Total fault = " , fault)
print ("Ratio for Hit" , hit/len(pages))
print ("Ratio for Fault" , fault/len(pages))


print ("\nMRU Page Replacement")

pages = [1,2,3,4,5,1,2,3,1]
cap  = 3
frame = []
recent = []
fault = 0
hit = 0
for page in pages:
    if page in frame:
        hit += 1
        print(page, "----->", frame, "Hit")
        recent.append(page)
        recent.remove(page)
    else:
        fault += 1
        if len (frame) < cap:
            frame.append(page)
        else:
            mru = recent [-1]
            frame.remove(mru)
            recent.remove(mru)

            frame.append(page)
        recent.append(page)

        print(page, "----->", frame, "Fault")
print ("Total Hits = " , hit)
print ("Total fault = " , fault)
print ("Ratio for Hit" , hit/len(pages))
print ("Ratio for Fault" , fault/len(pages))



