// X11Known_issues=['142235','136186','147646','147648','147650','146724','147719','147720','147721','147724','147725','147726','148001','133689','141808']


let Num=0
let IssueNums=['151509','151273','151508','147121'];

if (Num === 0){
    let IssueBox = document.getElementById('CBx_SearchIssueID'); 
    IssueBox.click();}

let IssueId = document.getElementById('Tx_SearchIssueID');
IssueId.value = '';
IssueId.value = IssueNums[Num];

let SubmitButton = document.getElementById('Bt_SearchIssue');
SubmitButton.click();

await new Promise(resolve => setTimeout(resolve, 4000));

let IssueLink = document.getElementById('GV_Issue_ctl03_LBt_IssueSubject4CPIS');
IssueLink.click();
await new Promise(resolve => setTimeout(resolve, 2000));
IssueLink.click();

console.log('['+IssueId.value+'] '+IssueLink.textContent);

issueTable = document.getElementById('GV_Issue').textContent
List = issueTable.split('\n ');
// console.log(List)
console.log('MB:'+List[54].trim());
console.log('Poster:'+List[56].trim())
console.log('Status:'+List[37].trim());

if ((Num+1) != IssueNums.length){
    console.log('剩'+(IssueNums.length - (Num+1))+'條issue');
} else {
    console.log('最後一條issue');
}