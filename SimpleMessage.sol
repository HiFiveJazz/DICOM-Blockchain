// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleMessage {
    string public message;

    function setMessage(string memory newMessage) public {
        message = newMessage;
    }
}

