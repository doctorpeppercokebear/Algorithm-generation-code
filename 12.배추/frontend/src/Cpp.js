import React from "react";
function Cpp(props) {
    let name = props.hello;
    const [time, settime] = React.useState(0);
    function updateTime()   {
        settime(time + 1);
        // time = time+1 => 이렇게 사용하면 에러 !!
    }
    return (
        <div> 
            <p>{name} world</p>
            <p>{time} </p>
            <button onClick={updateTime}>+1 올라가기</button>
    </div>
    );
}

export default Cpp;