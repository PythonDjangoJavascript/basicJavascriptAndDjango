
class App extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            num1: 1,
            num2: 1,
            response: "",
            score: 0
        };
    }

    render(){
        if (this.state.socre === 5) {
            return(
                <div>
                    <h1>Yeee! You Won!</h1>
                </div>
            );
        }

        return(
            <div id="problem">
                <div>{this.state.num1} + {this.state.num2}</div>
                <input onKeyPress={this.inputKeyPress} onChange = {this.updateResponse} value= {this.state.response}/>
                <div>Score: {this.state.score}</div>
            </div>
        );
    }

    updateResponse = (event) =>{
            this.setState({
                response: event.target.value
            });
        }
        inputKeyPress = (event) =>{
            if (event.key === 'Enter') {
                const answer = perseInt(this.state.response);
                if (answer === this.state.num1 + this.state.num2) {
                    this.setState(state => ({
                        score: state.score +1,
                        num1: Math.ceil(Math.random() * 10),
                        num2: Math.ceil(Math.random() * 10),
                        response: ""
                    }));
                }else{
                    this.setState(state => ({
                        score: state.score -1,
                        response: ""
                    }));
                }
            }
        }
}

