# Utilize a imagem oficial do Python como base
FROM python:3.9-slim

# Defina a variável de ambiente para garantir que o stdout e o stderr estejam disponíveis
ENV PYTHONUNBUFFERED=1

# Crie e defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o diretório de trabalho
COPY src/ .

# Expõe a porta em que a aplicação será executada
EXPOSE 5000

# Execute a aplicação
CMD ["python", "app.py"]
