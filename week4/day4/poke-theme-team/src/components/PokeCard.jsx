import { useState } from 'react';
import { useEffect } from 'react';
import ListGroup from 'react-bootstrap/ListGroup';
import { Card, Row, Col } from 'react-bootstrap';
import axios from 'axios';
import '../App.css'

function PokeCards({ pokemon, show }) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    
    useEffect(() => {
        const fetchData = async () => {
          try {
            const promises = pokemon.map(link => axios.get(link));
            const results = await Promise.all(promises);
            setData(results.map(result => result.data)); // Extract data from response
          } catch (err) {
            setError(err.message);
          } finally {
            setLoading(false);
          }
        };
    
        fetchData();
      }, [pokemon]);
    
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error: {error}</p>;

    
    

  return (
    <>
        {!show && (
            <div className='mt-4 bg-blue-900 p-4 rounded-2xl'>
            <Row className='flex flex-wrap'>
                {data.map((item, index) => (
                    <Col key={index} className='mb-4'>
                        <Card className='border-black'>
                            {item.sprites.front_default && (
                                <Card.Img variant='top' className='bg-red-700' src={item.sprites.front_default} alt= 'https://cdn.pixabay.com/photo/2016/07/23/13/18/pokemon-1536847_640.png'/>
                            )}
                            <Card.Body className='bg-amber-300'>
                                <Card.Title>{item.species.name}</Card.Title>
                            </Card.Body>
                            <ListGroup className='list-group-flush border-black'>
                                <ListGroup.Item className='border-black'>HP: {item.stats[0].base_stat}</ListGroup.Item>
                                <ListGroup.Item className='border-black'>Attack: {item.stats[1].base_stat}</ListGroup.Item>
                                <ListGroup.Item className='border-black'>Defense: {item.stats[2].base_stat}</ListGroup.Item>
                                <ListGroup.Item className='border-black'>Special Attack: {item.stats[3].base_stat}</ListGroup.Item>
                                <ListGroup.Item className='border-black'>Special Defense: {item.stats[4].base_stat}</ListGroup.Item>
                                <ListGroup.Item className='border-black'>Speed: {item.stats[5].base_stat}</ListGroup.Item>
                            </ListGroup>
                        </Card>
                    </Col>
                ))} 
            </Row>
            </div>
        )}
    </>   
  );
}

export default PokeCards;