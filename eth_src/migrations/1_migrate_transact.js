const MyContract = await ethers.getContractFactory("transact");
this.myContract = await MyContract.deploy();