//pragma solidity >=0.4.25 <0.6.0;
pragma experimental ABIEncoderV2;
contract election
{
    enum StateType {enrolling, enrolled, voting, voted}

    StateType public  State;
    struct CandidateStruct {
        int CandidateID;
        int VoteInFavour;
    }
    
    CandidateStruct[] CandidateList;
    address public Voter;
    address public Admin;

    constructor(address admin) public {
        Admin = admin;
        State = StateType.enrolling;
    }

    function addCandidate(int CandidateID, bool finished) public {
        CandidateList.push(CandidateStruct(CandidateID, 0));
        if (finished){
        State = StateType.voting;
        }
    }

    function publishCandidateList() public {
        int totalVotes = 0;
        for (uint i = 0; i < CandidateList.length; i++) {
            totalVotes = totalVotes + CandidateList[i].VoteInFavour;
        }
    }

    function addVote(int CandidateID, bool finished) public {
        for (uint i = 0; i < CandidateList.length; i++) {
            if (CandidateList[i].CandidateID == CandidateID) {
                CandidateList[i].VoteInFavour++;
                break;
            }
        }
        if (finished){
        State=StateType.voted;
        }
    }
}