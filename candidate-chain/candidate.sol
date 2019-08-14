pragma experimental ABIEncoderV2;
contract candidate
{
    enum StateType {enrolling, enrolled}

    StateType public State;
    struct CandidatePersonalDetails{
        string name;
    }
    struct CandidateStruct {
        int CandidateID;
        //CandidatePersonalDetails details;
    }
    
    CandidateStruct[] public CandidateList;

    address public Admin;

    constructor(address admin) public {
        Admin = admin;
        State = StateType.enrolling;
    }

    function addCandidate(int CandidateID, bool finished) public {
        CandidateList.push(CandidateStruct(CandidateID));
        if (finished){
        State = StateType.enrolled;
        }
    }   

    function publishCandidateList() public {
        //return CandidateList;
    }

}