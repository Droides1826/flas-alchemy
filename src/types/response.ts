
// Limit nombres 30
// Limit Response 255


interface Categoria {
	descripcion: string
	id_categoria: number
	nombre: string
}


enum CodigoStatus {
	200,
	401,
	404,
	500,
	409
};


// Status enum aqui

interface Response {
	message: string
	status: CodigoStatus
	data: Categoria[]
}
