import React from 'react';
import './Table.css';

function Table({tableData}){
    return(
        <table className='table'>
            <thead className='thead'>
                <tr className='tr-head'>
                    <th className='th'>Data</th>
                    <th className='th'>Operação</th>
                    <th className='th'>Saldo após Movimento</th>
                    <th className='th'>Descrição</th>
                </tr>
            </thead>
                <tbody className='tbody'>
                    {tableData.map((value, index)=>{
                        return(
                            <tr className='tr-body' key={index}>
                                <td className='td'>{value.date}</td>
                                <td className='td'>{value.value}</td>
                                <td className='td'>{value.saldoapos}</td> {/* TODO mudar para saldo */}
                                <td className='td'>{value.description}</td>
                            </tr>
                        )
                    })}
                </tbody>
        </table>
    )
}
export default Table;