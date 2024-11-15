#ifndef CLIENTE_H_ICLUDED
#define CLIENTE_H_ICLUDED

class Cliente{
    public:
    void MudaCPF(std::string cpf);
    void GetDados();

    private:
    std::string nome;
    std::string endereco;
    std::string cpf;
    int idade;
    bool validarCPF(std::string cpf);
    
};
void Cliente::MudaCPF(std::string cpf){
    if(this->validarCPF(cpf)){
        this->cpf = cpf;
    }
}

void Cliente::GetDados(){
    std::cout<<this->nome<< "\n";
    std::cout<<this->endereco<< "\n";
    std::cout<<this->cpf<< "\n";
    std::cout<<this->idade<< "\n";


}

bool Cliente::validarCPF(std::string cpf){
    return true;
}
#endif