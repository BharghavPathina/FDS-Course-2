class SavingsAccount:
    """
    Bank is a class with certain properties and actions

    Properties: ---- Member Variables -- States
        1. AccountHoldersName
        2. AccountNumber
        3. AccountType
        4. Balance
        5. AccountHoldersContactNumber

    Actions: ---- Member Methods / Member Functions -- Behaviours
        1. withdraw
        2. deposit
        3. check balance


    OOPS class have higher access control -- access specifiers
    """

    

    """
        These class properties are global properties
    """

    __accountName = None
    __accountNumber = None
    _accountPhoneNumber = None
    accountType = None
    __balance = None

    """
    Constructor will be called while creating the object
    """
    def __init__(self,accountName=123,phoneNumber=123,balance=123,type="savings") -> None: 

        """
        Properties inside constructor are instacne properties --- specific to object
        """
        self.__accountName = accountName
        self.__accountNumber = "123456789"
        self._accountPhoneNumber = phoneNumber
        self.accountType = type
        self.__balance = balance

    def show_details(self):
        print("Details of Account Holder:")
        print(f"Name:{self.__accountName}")
        print(f"Phone Number:{self._accountPhoneNumber}")
        print(f"Account Type: {self.accountType}")

    def set_accountName(self,name):
        self.__accountName = name

    def get_accountName(self):
        return self.__accountName

    def widthdraw(self):
        pass
    def deposit(self):
        pass
    def check_balance(self):
        pass


malyadriAccount = SavingsAccount()  ## Object Initializing State -- First Object State
malyadriAccount.accountType = "hsdbsdh"
malyadriAccount.show_details()

# malyadriAccount.set_accountName("Malyadri Kumar")
# malyadriAccount.show_details()