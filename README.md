# CFD-19-IITJ
Repository for Microsoft code.fun.do++ project '19

Team Name: Millenium Falcon

College: IIT Jodhpur

Team: Anshul Ahuja, Siddhant Saoji & Chakshu Gupta

## Our project consists of 2 broad parts:

### Blockchain Aadhar
Using the Azure blockchain service to keep a track of all Indian citizens and their biometric data. This is basically a blockchain alternative of Aadhar. We intend to use the Azure workbench to expose REST APIs with restricted verification only access to the blockchain. The aadhar service would also publish population demographics using Azure Power BI service.

### Voting Blockchain
This would be another blockchain. As per the Aadhar blockchain, after every citizen turns above the age of 18, their digital voter ID would automatically be generated while ensuring mobility of vote across the nation. We intend to create *EVMs based on IOT devices using Azure IOT Core service*. The EVM would be based on Raspberry Pi (in future AzureSphere). The device would communicate using the REST APIs by Azure Blockchain workbench to vote directly on the blockchain while updating the Aadhar blockchain indicating that the person has voted.
The voting data(total votes) would be shown in real time using Azure Power BI analytics service.

