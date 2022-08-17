import csv
lijst= {}
with open('title-episodes.tsv','r',encoding='utf-8') as episode:
    reader = csv.DictReader(episode,delimiter='\t')
    optelling = 0
    for row in reader:
        if(row['parentTconst'] not in lijst):
            lijst[row['parentTconst']]=0
        lijst[row['parentTconst']]+=1
sort_orders = sorted(lijst.items(), key=lambda x: x[1], reverse=False)
niet_verwijderd=sort_orders.copy()
with open('title-basics.tsv', encoding='utf-8') as basic:
    reader= csv.DictReader(basic,delimiter='\t')
    for i in sort_orders:
        for line in reader:
            if i[0] == line['tconst']:
                if line['titleType'] != 'movie':
                    sort_orders.remove(i)

                break;
uitvoer1 = 0
uitvoer2=0
with open('niet.txt','w') as uitvoer:
    for i in niet_verwijderd:
        uitvoer.write(str(i))
        uitvoer1+=1
with open('gesorteerd.txt','w') as uitvoer:
    for i in sort_orders:
        uitvoer.write(str(i))
        uitvoer2+=1
print(str(uitvoer1)+":"+str(uitvoer2))

