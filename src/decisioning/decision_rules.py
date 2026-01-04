def decision(risk):
    if risk == "Low Risk":
        return "Approve"
    elif risk == "Medium Risk":
        return "Manual Review"
    else:
        return "Reject"
