pragma solidity ^0.4.15;

contract SmartBar {
    address owner = msg.sender;
    uint price = 0.01 ether;
    uint beers;

    event GetBeer(uint indexed beer);

    function () payable {
        require((1 ether * msg.value/price) % 1 ether == 0);
        beers = msg.value/price;
        GetBeer(beers);
    }
    
    function payout() {
        require(msg.sender == owner);
        owner.transfer(this.balance);
    }
}
