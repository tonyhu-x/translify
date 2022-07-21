export default function TransBox(props) {
  const text = props.text;
  const out = props.out;
  const onChange = props.onChange;

  const onTextChange = (e) => {
    onChange(e.target.value);
  };
  
  return (
    <textarea className="font-sans shadow" disabled={out} onChange={onTextChange} value={text}></textarea>
  );
};