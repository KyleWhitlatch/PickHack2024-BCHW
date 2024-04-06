// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;


contract transact{

    struct CryptoData{
        string cpu_id;
        string gpu_id;
        string mobo_id;
    }

    CryptoData userdata; 
    string hash_comp;

    constructor(


    ) {

    }

    function hashGenerator(string calldata str) pure external returns (bytes32){
        return keccak256(abi.encodePacked(str));
    }

    function compareHash(string calldata ext_hash) external view returns (bool) {
        return keccak256(abi.encode(hash_comp)) == keccak256(abi.encode(ext_hash));
    }


}