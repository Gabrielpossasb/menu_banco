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

## 🖥 Demonstração  

Veja abaixo como o sistema funciona no terminal:  

### 🏦 Menu Bancário  

<p align="center">
  <img src="https://github.com/user-attachments/assets/b8de1cb9-cea5-4952-973c-9122f71db888" width="200px">
</p>

---

<div align="center">

<table>
  <tr>
    <td align="center"><strong>💰 Realizando um Depósito</strong></td>
    <td align="center"><strong>💸 Realizando um Saque</strong></td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/45a0daef-51b2-4672-93a3-ea6f33bcd2e1" width="100%">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/fa9a871b-1abc-4502-b88b-8ff4ac4810eb" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center"><strong>🏦 Saque no Cheque Especial</strong></td>
    <td align="center"><strong>📜 Visualizando o Extrato</strong></td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/d0950fbf-fbaa-4958-8898-8364b71a4e89" width="100%">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/7d2e0724-2490-41fa-ade9-3af0538c44de" width="100%">
    </td>
  </tr>
</table>

</div>


