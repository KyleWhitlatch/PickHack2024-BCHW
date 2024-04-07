// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;


contract transact{

    bytes32 hash_comp;

    constructor(string memory str_to_hash) {
        hash_comp = keccak256(abi.encodePacked(str_to_hash));
    }

    function hashGenerator(string calldata str) pure external returns (bytes32){
        return keccak256(abi.encodePacked(str));
    }

    function compareHash(bytes32 ext_hash) external view returns (bool) {
        return hash_comp == ext_hash;
    }
    function gethash() view external returns (bytes32){
        return hash_comp;
    }


}