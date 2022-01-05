pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
contract MyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;
    Counters.Counter private _tokenIds;
    mapping (uint256 => string) private _tokenURIs;
    
    bytes32  check1 = "";
    bytes32  check2 = "";
    
    string  answer = "";
    
    string latitudelongitude;

    
    struct riddle {
        bytes32 hash;
        string uri;
        
    }

    
    mapping (string => riddle ) riddle_location;
    
    constructor() ERC721("SuCrypture", "SuC") {
        
        riddle memory riddle1 = riddle(bytes32(0xDDD86EE4267967426EC4E90E350D926D9BEF0837F1509CBA4211208DA613BD39), "https://upload.wikimedia.org/wikipedia/tr/d/d3/Sabanc%C4%B1_%C3%9Cniversitesi_logosu.jpg");
        
        riddle memory riddle2 = riddle(bytes32(0xBC6213415AC75DE11DFF6B022B774E446133F51E69A780D7A5C060377E4EEDB1), "https://upload.wikimedia.org/wikipedia/tr/d/d3/Sabanc%C4%B1_%C3%9Cniversitesi_logosu.jpg");
        
        riddle memory riddle3 = riddle(bytes32(0x080F0C7C7DE688E2439716EA2FB17C7673A54E8BA4A3A25DCABE9060FBEEBB89), "https://upload.wikimedia.org/wikipedia/tr/d/d3/Sabanc%C4%B1_%C3%9Cniversitesi_logosu.jpg");
        
        riddle memory riddle4 = riddle(bytes32(0xCAAD66E439990930CB465E9DF5D24F56CE1CAB37CC534A8AD6BE31FE7662694A), "https://upload.wikimedia.org/wikipedia/tr/d/d3/Sabanc%C4%B1_%C3%9Cniversitesi_logosu.jpg");
        
        riddle memory riddle5 = riddle(bytes32(0x02F82CA7CC561667571EE8EB9710A65D2E2626617DEF9221D9D234B59144188E), "https://upload.wikimedia.org/wikipedia/tr/d/d3/Sabanc%C4%B1_%C3%9Cniversitesi_logosu.jpg");
        
        riddle memory riddle6 = riddle(bytes32(0xB8AC3FEC8A935198BACFD7FAC7CD287E5EE07C6A1948734C1A041FAA4ED93419), "https://upload.wikimedia.org/wikipedia/tr/d/d3/Sabanc%C4%B1_%C3%9Cniversitesi_logosu.jpg");
        
        riddle memory riddle7 = riddle(bytes32(0x6997E0761368883110032E0CC3D21DA437E6220329E19210CD924560F7BFEECB), "https://upload.wikimedia.org/wikipedia/tr/d/d3/Sabanc%C4%B1_%C3%9Cniversitesi_logosu.jpg");
        
        riddle memory riddle8 = riddle(bytes32(0x963971D4479B59024BDA3870678F33F2A59A772C5B263E92A12046AB472BD4DD), "https://upload.wikimedia.org/wikipedia/tr/d/d3/Sabanc%C4%B1_%C3%9Cniversitesi_logosu.jpg");
        
        riddle memory riddle9 = riddle(bytes32(0xAD282BFF8B09165E5C69203E64C14703DB3B852BB4521345C65EFFF3C1D7B21E), "https://upload.wikimedia.org/wikipedia/tr/d/d3/Sabanc%C4%B1_%C3%9Cniversitesi_logosu.jpg");
        
        
        //galata tower   41.025658,28.974155
        riddle_location['Long tower from ancient times. You can climb or jump and fly.'] = riddle1;
        //blue mosque    41.0054096,28.9768138
        riddle_location["Feel the tile blue. Where are you?"] = riddle2;
        //topkapi        41.0115195,28.9833789
        riddle_location["A palace of sultans' that welcomes all visitors. You do hesitate until you see the ..."] = riddle3;
        //Sabanci University   40.8924593,29.3753831
        riddle_location["A missed place where successful students belongs."] = riddle4;
        //Dolmabahçe     41.0391643,28.9982707
        riddle_location["A palace that float on the Bosphorous."] = riddle5;
        //Hagia Sophia   41.008583,28.9779863
        riddle_location["Oh holy wisdom, how big wonders are built for you. "] = riddle6;
        //Kız Kulesi     41.0139242,28.9837942
        riddle_location["A lonely girl who is improsined a tower and waits her prens. But her waiting did not last long and by a snake, it ends."] = riddle7;
        //Çemberli taş   41.0085363,28.9692432
        riddle_location["A granite column which is surrounded by brackets. If you look closer, you can see emperor Constantine maybe."] = riddle8;
        //Yılanlı taş    41.0060728,28.9730869
        riddle_location["It is the symbol of the victory. One column, 3 twisting snakes and 31 Ancient Greek Cities"] = riddle9;
        
        
        
    }
    
    function _setTokenURI(uint256 tokenId, string memory _tokenURI)
    internal
    virtual
        {
        _tokenURIs[tokenId] = _tokenURI;
        
        
        
        
    }
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory)
    {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        string memory _tokenURI = _tokenURIs[tokenId];
        return _tokenURI;
    }
    
    function mint(address recipient, string memory uri) public returns (uint256)
    {
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();
        _mint(recipient, newItemId);
        _setTokenURI(newItemId, uri);
        return newItemId;
    }
  

    function substring(string memory str, uint startIndex, uint endIndex) private returns (string memory) {
        bytes memory strBytes = bytes(str);
        bytes memory result = new bytes(endIndex-startIndex);
        for(uint i = startIndex; i < endIndex; i++) {
            result[i-startIndex] = strBytes[i];
        }
        return string(result);
    }

    
 
    function remove_two_digits (string memory user_latitude, string memory user_longitude) private returns(string memory) {
        latitudelongitude = string(abi.encodePacked(substring(user_latitude, 0, bytes(user_latitude).length -2 ), ',', substring(user_longitude, 0, bytes(user_longitude).length -2 )));
        
        return string(abi.encodePacked(substring(user_latitude, 0, bytes(user_latitude).length -2 ), ',', substring(user_longitude, 0, bytes(user_longitude).length -2 )));
    } 


    
    function location_check (string memory riddle, string memory user_latitude, string memory user_longitude) public  {
    answer = remove_two_digits(user_latitude, user_longitude);
        //bytes32 memory = sha256(abi.encodePacked(answer));
        //string memory hash_var = string(;
        
        check1 = sha256(bytes(answer));
        check2 = riddle_location[riddle].hash;
       
        if  (sha256(bytes(answer)) == riddle_location[riddle].hash) {
            mint(msg.sender, riddle_location[riddle].uri);
            
        }
    }
    

  
}