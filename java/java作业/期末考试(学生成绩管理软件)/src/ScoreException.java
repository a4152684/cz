public class ScoreException extends Exception {
    String err;
    ScoreException()
    {
        err="成绩应在0-100之间";
    }
    public String get_err()
    {
        return err;
    }
}
