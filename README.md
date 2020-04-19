# :godmode: :man: :woman: :older_man: Codificação de Rostos
Projeto da área de visão computacional que visa o estudo de processos análogos ao hashing para codificação de rostos.

## :family: Team
[Caio Netto]()
[Eduardo Eiras](https://github.com/dueiras)
[Luísa Heise](https://github.com/luisaheise)
[Paulo Sestini](https://github.com/paulosestini)
[Rodrigo Estevam](https://github.com/materloki)
[Rodrigo Fill](https://github.com/rodrigofill)
[Victor Jinsi]()

## :seedling: Proposta
O banco BTG Pactual nos propôs um projeto para solucionar um problema específico de comunicação entre bancos. 
É de interesse dos bancos saber informações sobre seus novos clientes, como se ele tem um mal histórico com outros bancos.
Para trocar informações entre bancos é necessário que essa informação seja codificada de maneira que a identidade do usuário se mantenha anônima. Ou seja, em cima da informação terá de haver algum tipo de codificação, para que se houver interceptação na comunicação, as informações se manterem privadas.
Isso já é feito com informações como CPF ou RG (na forma de uma codificação hash), mas o BTG vê interesse em fazer tal codificação com o rosto do usuário, então esse é o nosso desafio.

## :flashlight:	Escopo
O projeto visa criar um sistema que recebe uma foto do usuário e codifica essa informação com uma operação que não permita a reconstrução da imagem.
Como pode haver inúmeras variáveis de condições das fotos, optamos por limitar as opções de imagens a serem analisadas:
    - Rostos em posição frontal;
    - Condição de iluminação parecida;
    - Usuário com expressão neutra.

## :game_die: Estratégia Inicial
Nossa abordagem inicial é tentar replicar um paper antigo, de 1996, que categoriza rostos de pessoas com base em distâncias entre pontos do rosto. Neste paper essas distâncias são extraídas “a mão”, o que é totalmente inviável para nosso projeto.
Tirando essas informações das imagens de forma automática (seja com ML ou com CV clássica), utilizaremos essas informações como código para definir a identidade da pessoa

## :hammer: Pipeline
Inicialmente pretendemos montar o programa que irá identificar as landmarks faciais, esse programa provavelmente será feito com uma rede neural, seja ela treinada por nós ou pré-treinada. Com os pontos, seguiremos a tabela de distâncias presente no paper para extrair as features para classificação. Por fim pretendemos encontrar formas diferentes de classificação com base nestas, seja implementando a proposta do paper, de mixture distances, seja por outras formas de classificação, uma possível é, por exemplo, um KNN. 

## :heavy_check_mark: O que foi feito até o momento
    • Estudo de técnicas de transformada hash em imagens;
    • Métodos de reconhecimento facial;
    • Aplicação de métodos simples com CV clássico;
    • Estudo da biblioteca dlib, com aplicações em identificação de landmarks e extração de distâncias;
