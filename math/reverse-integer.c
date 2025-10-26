int reverse(int x){

    if (x == INT_MIN){
        return 0;
    }

    int ret = 0;

    bool neg = false;
    if (x < 0){
        neg = true;
        x *= -1;
    }

    while (x > 0){

        if (ret > INT_MAX/10){
            return 0;
        }

        ret *= 10;
        ret += x%10;
        x /= 10;


    }

    if (neg) return ret*-1;

    return ret;



}