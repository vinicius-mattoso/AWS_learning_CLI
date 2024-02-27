# Etapas para conseguir acessar via código python a interface da AWS

1. Vamos precisar criar um IAM User.

    Dentro do console vai para IAM > User > CreteUser
        Você vai ter duas opções, ou colocar esse novo usuário junto a um grupo de usuários cada um com suas executions role ou vai Attach uma policies especial para ele:
    ![alt text](image.png)

    Vou seguir esse tutorial e por isso vou dar um attach para ele.
    ![alt text](image-1.png)

    Ai agora você precisa ir liberando o que você deseja, por exemplo na imagem acima só liberou o acesso ao S3, será que só com esse da para acessar o SageMaker?? Ou será necessário utilizar essa autorização:
    ![alt text](image-2.png)

    Nos tutoriais eles já concedem direto esse acesso total:
    ![alt text](image-3.png)

    Agora você precisar criar uma acess Key para conseguir fazer a comunicação.
    ![alt text](image-4.png)
    Você precisa autorizar o acesso desse user via CLI da seguinte maneira:
    ![alt text](image-5.png)

    Após a criação você deve configurar no seu terminal da seguinte maneira:

    ![alt text](image-6.png)

    *OBS* Vale a pena criar um arquivo .env para salvar as variaveis de ambientes necessárias para a conexão ao SageMaker e também para configurar o CLI.
    ![alt text](image-7.png)
    Para acessar essas variáveis se faz necessário a lib : python-dotenv para ter acesso ao método load_dotenv.


2. Acessar o S3 para guardar dados e modelos

    Para se criar um novo bucket você deve fazer:
    ![alt text](image-8.png)

    Para conseguir visualizar a lista de bucket que aquele usuário tem naquela região deve:

    ![alt text](image-9.png)

    Vou esperar 1 hora para ver se sou taxado, depois vou tentar subir arquivos para esse bucket via terminal tbm.
    Nada de novo na minha fatura kkk

3. Subir arquivos para o bucket
    



    

    ACESS: AKIA2UC3ERNNN257FEG6
    KEY : LXek45xSeLexl9RPmu9e8Xtb35LKxG8ptE3eQB3i
    REGIO: us-east-1 -> N. Virginiak