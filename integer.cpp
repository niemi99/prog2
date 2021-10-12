#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib_cpp();
	private:
		int val;
		int fib_cpp_private(int);
	};

int Integer::fib_cpp(){
	return fib_cpp_private(val);
} 
int Integer::fib_cpp_private(int n){
	if (n <= 1){
		return n;
	}
	else {
		return (fib_cpp_private(n-1)+fib_cpp_private(n-2));
	}
}
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_fib_cpp(Integer* integer){return integer -> fib_cpp();}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}