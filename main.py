from pay import PayClass

callPay = PayClass.momopay(1500, "EUR", "1234test", "0757889291", "Finish Your Transaction")
ref = callPay["ref"]

if callPay["response"] == 200 or callPay["response"] == 202:

# Verify the transaction
    verify = PayClass.verifymomo(callPay["ref"])
    if verify["status"] == "SUCCESSFUL":
        print("Thanks for your transaction!")
    else:
        print("Transaction Failed!")
else:
    print("Transaction not valid for this transaction!")

#Checking the collections balance
checkcollectionsbalance = PayClass.momobalance()
print(checkcollectionsbalance)

#Transfer money from disbursement account
withdrawmoney = PayClass.withdrawmtnmomo("10", "EUR", "col23", "0780909566", "Done!")
print(withdrawmoney["response"])



# {
#  "amount": 100,
#  "currency": "UGX",
#  "financialTransactionId": 23503452,
#  "externalId": 947354,
#  "payer": {
#    "partyIdType": "MSISDN",
#    "partyId": 4656473839.0
#  },
#  "status": "SUCCESSFUL"
# }