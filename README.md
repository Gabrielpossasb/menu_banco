# 📌 Simulador de Menu Bancário  

Este projeto foi desenvolvido como parte do **Bootcamp da empresa Suzano na plataforma DIO (Digital Innovation One)**, dentro do módulo **"Sintaxe Básica com Python"**.  

O desafio consistia em criar um sistema bancário simples com funcionalidades de **depósito, saque e extrato**. Além das regras básicas fornecidas no desafio, **algumas extras foram adicionadas**.  

## 🛠 Funcionalidades  

✔️ **Depósito**  
- Apenas valores positivos podem ser depositados.  
- Todos os depósitos são registrados no extrato.  

✔️ **Saque**  
- O usuário pode realizar até **3 saques por dia**.  
- O limite máximo para cada saque é de **R$ 500,00**.  
- O sistema notifica caso o saldo não seja suficiente para a operação.  
- Todos os saques são registrados no extrato.  

✔️ **Extrato**  
- Lista todos os depósitos e saques realizados.  
- Exibe o saldo atual da conta.  
- Caso não haja movimentações, exibe a mensagem: `"Não foram realizadas movimentações."`  
- Todos os valores são exibidos formatados com **duas casas decimais e o símbolo R$**.  

### 🔹 Funcionalidades Extras Adicionadas
⭐ **Limite máximo de depósito: R$ 5.000,00** → Impede depósitos acima desse valor.  
⭐ **Horário nas transações** → Cada saque e depósito agora exibe a hora exata da operação.  
⭐ **Cheque especial** → Permite saques mesmo sem saldo, até um limite de **-R$ 500,00**.
