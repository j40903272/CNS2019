from random import randint

with open('./flag') as f:
    flag = f.read()

p = 28661294800114069007768236017771012251607018576093986823286814149509513675452275635042638987354048629725185006983949952108837417118101024196427874059746112373146674688108102191658628381225899560628677933856157056627887468689106995559937935463599189450455206845179774222254667824788120465189001600194073757297794949787319524466635098273575710447185401574795742616708210395524755264624260682423348748123914632427585203446721466593339015399125761744284777424125509546314701569108898934480431326685681803242146702497611445457941195705272186806178159360836165609438994389786824034040397877095231384671425898312053134662669
print 'p =', p
#g = 2
g = 16078909570239876795055844516958246040709670677352681543313753053742973386508316274779434207505711677850871497649465535051866957457021948204451138330623660110191150301811323442658421231468580615274747861693791813916691182214785963319378314164808593693096050898468910883788576053845247354173273067934871765729622501051769175928793373665854926345829773055861683607699372255679226577615328998611278891869859367786539895393361508257631990706373751978989473197793935179727162255300656316829056421905796513359716410495375718068635872275352455310154328769091838733283528171239199077479704783804081954231420368626696801127642
print 'g =', g

a = randint(1, p-1)
A = pow(g, a, p)
print 'A =', A
B = input('Enter the public key you recieved: ')
print 'B =', B
s = pow(B, a, p)

print 'cipher =', (int(flag.encode('hex'), 16)*s)%p