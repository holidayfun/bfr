header_type bier_t {
  fields {
    first_nibble : 4;
    Ver : 4;
    Len : 4;
    Entropy : 20;
    BitString : *;
    OAM : 2;
    Reserved : 10;
    Proto : 4;
    BFIR_id : 16;
  }
  length: 32 + 2^(Len + 5) + 32 ; /* 32 bit vor  BitString, Länge des BitString, 32 Bit nach BitString */
}

header_type ethernet_t {
  fields {
    dstAddr : 48;
    srcAddr : 48;
    etherType : 16;
  }
}

header_type ipv4_t {
  fields {
    version : 4;
    ihl : 4;
    diffserv : 8;
    totalLen : 16;
    identification : 16;
    flags : 3;
    fragOffset : 13;
    ttl : 8;
    protocol : 8;
    hdrChecksum : 16;
    srcAddr : 32;
    dstAddr : 32;
  }
}
