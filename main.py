from time import sleep 

from hypot import cos, math, sin, radians, tan

from datetime import date


from random import randint, shuffle, choice

def desafio001():
  return 'Olá, Mundo!'



def desafio002():
  nome = input('Digite seu nome: ')
  return f'É um prazer te conhecer, {nome}!'


def desafio003():
  
  n1 = int(input("digite um valor:"))
  n2 = int(input("digite outro valor:"))
  s = n1+n2
  print("a soma entre {} e {} é igual a {}".format(n1, n2, s))



def desafio004():
  
  a = input("digite algo:")
  print("tipo primitivo:", type(a))
  print("só tem espaço", a.isspace())
  print("é um número:", a.isnumeric())
  print("é alfabético:", a.isalpha())
  print("é afanúmerico:", a.isalnum())
  print("maiusculas:", a.isupper())
  print("minuscula:", a.islower())
  print("capitalizado:", a.istitle())




def desafio005():
  n = int(input('Digite um número'))

  return f'analisando o valor {n}, seu antecessor é {n-1} e o sucessor é {n+1}'

def desafio006():
  n = int(input('Digite um número'))

  print(f' 0 dobro de {n} vale {n*2}.')
  print(f' 0 dobro de {n} vale {n*3} \n A raiz quadrada de {n} é igual a {n**(1/2)}.')


def desafio007():
  n1 = float(input('primeira nota do aluno: '))
  n2 = float(input('segunda nota do aluno: '))
  = (n1 + n2 / 2)

  return 'A média entre {:.if} e {:.if} é igual a'


def desafio009():
  n = int(input('Digite um número para ver sua tabuada:'))

  print('_' * 12)
  print('{} * {:2} = {}'.format(n, 1, n*1))
  print('{} * {:2} = {}'.format(n, 2, n*2))
  print('{} * {:3} = {}'.format(n, 3, n*3))
  print('{} * {:4} = {}'.format(n, 4, n*4))
  print('{} * {:5} = {}'.format(n, 5, n*5))
  print('{} * {:6} = {}'.format(n, 6, n*6))
  print('{} * {:7} = {}'.format(n, 7, n*7))
  print('{} * {:8} = {}'.format(n, 8, n*8))
  print('{} * {:9} = {}'.format(n, 9, n*9))
  print('{} * {:10} = {}'.fotmat(n, 10, n*10))
  print('_' * 12)



  def desafio010():
    real = float(input('Quanto dinheiro você tem na carteira? R$'))
    dolar = real / 5.06
    euro = dolar / 5.74

  return 'com R${:.2f} pode comprar US${:.2f} e também €{:.2f}'.format(real, dolar, euro)



def desafio011():
  larg = float(input('largura da parede: '))
  alt = float(input('altura da parede: '))
  área = larg * alt
  print(f'sua parede tem a dimensão de {larg}x{alt} e sua área é de [área]m2')
  tinta = área / 2 
  print(fpara pintar a parede, você precisará de {tinta}1 de tinta')


def desafio012():
  c = float(input('Qual é o preço do produto? R$'))
  novo = preço - (preço * b5 / 100)

  return '0 produto que custava R${:.2f}, na promoção de 5% vai custanR${:.2f}'.format(preço, novo)



def desafio013():
  sálario = float(input('qual é o salário do funcionário R$'))
  novo = salário + 15 / 100)
  return 'Um funcionário que ganhava R${:.2f}', com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo)


def desafio0014():
  c = float(input('informe a temperatura em °C: '))
  f = 9 * c / 5 * 32
  return f'A temperatura de {c}°C corresponde a {f}°F!'



def desafio015():
  dias = int(input('quantos dias alugados '))
  km = float(input('quantos km rodados? '))
  pago = (dias * 60) * (km * 0.15)
  return '0 total a pagar é de R${:.2f}'.format(pago)



def desafio0016():
  num = float(input('Digite um valor'))
  return '0 valor digitado foi de {} e sua porção
  inteira é {}'.format(num, int(num))



def desafio017():
    co = float(input('Comprimento do cateto oposto: '))
    ca = float(input('Comprimento do cateto ajacente: '))
    hi = hypot(co , ca)
    return ' A hipotenusa vai medir {:.2f}'.format(hi)



def desafio018():
    angulo = float(input('Digite o angulo que você desaja: '))
    seno = sin(radians(angulo))
     print('0 ângulo de {} tem SENO de {:.2f}'.format(âgulo, seno))
     cosseno = cos(randians(ângulo))
     print('0 ângulo de {} tem COSSENO de {:.2f}'.format(ângulo, cosseno))
     tangente = tan(radians(ângulo))
     print('0 ângulo de {} tem TANGENTE de {:.2f}'.format(ângulo, tangente))



def desafio019():
  
  from random import choice

  a1 = input("primeiro aluno:")
  a2 = input("segundo aluno:")
  a3 = input("terceiro aluno:")
  a4 = input("quarto aulno:")
  l = [a1, a2, a3, a4]
  e = choice(l)

  print("o aluno sorteado foi {}".format(e))

  


def desafio020():

  from random import shuffle

  a1 = input("primeiro aluno:")
  a2 = input("segundo aluno:")
  a3 = input("terceiro aluno:")
  a4 = input("quarto aulno:")
  l = [a1, a2, a3, a4]
  shuffle(l)
  print("ordem de apresentação será ")
  print(l)  




def desafio022():
  
  n = input("seu nome:").strip()
  print("analisando...")
  print("nome em maiúsculo: {}".format(n.upper()))
  print("nome em minúsculo: {}".format(n.lower()))
  print("nome tem {} letras".format(len(n) - n.count(" ")))
  s = n.split()
  print("o primeiro nome é {} e ele possui {} letras".format(s[0], len(s[0])))





def desafio024():
  
  c = input("qual cidade você nasceu?:").strip()
  print(c[:5].upper() == "SANTOS")



  def desafio025():
  
  n = input("nome completo:").strip()
  print("esse nome tem Oliveira? {}".format("Oliveira" in n.lower()))



  def desafio026():
  
  f = str(input("digite uma frase:")).upper().strip()
  print("quantidades de vezes que aparece a letra 'A' {}".format(f.count('A')))
  print("a primeira letra 'A' apareceu nessa posição {}".format(f.find('A') +1 ))
  print("a ultima letra 'A' apareceu nessa posição {}".format(f.rfind('A') +1 ))




  def desafio027():

  n = str(input("nome completo:")).strip()
  name = n.split()
  print("é um prazer te conhecer")
  print("primeiro nome: {}".format(name[0]))
  print("ultimo nome: {}".format(name[len(name) -1]))





def desafio028():

  from random import randint

  comp = randint(0,5)
  print("=====================")
  print("adivinhe o numero 'dica: é um numero entre 0 e 5'")
  print("====================")

  jog = int(input("bora adivinha ai:"))

  if jog == comp:
    print("PARABÉNS!!!")

  else:
    print("ERROU!!")

def desafio029():

  v = float(input("velocidade atual do seu automóvel:"))

  if v > 80:
    print("MULTADO! você passou do limite de velocidade")

    m = (v - 80) * 7

    print("sua multa é de R${}".format(m))




def desafio030():

  num = int(input("número:"))
  r = num % 2

  if r == 0:
    print("o numero {} é PAR".format(num))

  else:
    print("o numero é {} é IMPAR".format(num))





def desafio031():

  d = float(input("qual a distancia da sua viagem?:"))
  print("você vai comecar sua viagem de {}km".format(d))
  p = d * 0.05  if d <= 200  else d * 0.45
  print("sua passagem custará R${}".format(p))




def desafio032():

  from datetime import date

  a = int(input("qual ano quer que seja analizado? caso queria analisar o ano atual digite 0 :"))

  if a == 0:
    a = date.today().year

  if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("o ano {} é bissexto".format(a))

  else:
    print("o ano {} não é bissexto".format(a))





def desafio033():

  p = int(input("primeiro valor:"))
  s = int(input("segundo valor:"))
  t = int(input("terceiro valor:"))
   
  m = p 
  if s < p and s < t:
    m = s

  if t < p and t < s:
    m = t

  
  ma = p
  if s > p and s > t:
    ma = s

  if t > p and t > b:
    ma = t 

  print("menor valor digitado {}".format(m))
  print("maior valor digitado {}".format(ma))






def desafio034():

  s = float(input("qual o salario do funcionario?: R$"))

  if s <= 1250:
    n = s + (s * 15 / 100)

  else:
    n = s + (s * 10 / 100)

  print("quem ganhava R${} passou a ganhar R${}".format(s, n))






def desafio035():

  print("analisando o triangulo...")

  r1 = float(input("primeiro comprimento:"))
  r2 = float(input("segundo comprimento:"))
  r3 = float(input("terceiro comprimento:"))

  if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("pode ser feito um triangulo")

  else:
    print("não pode ser um triangulo")
