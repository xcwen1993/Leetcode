public class AddDigits {
    public int addDigits(int num) {
        int n = num%9;
        return (n==0)?((num==0)?0:9):n;
    }
}