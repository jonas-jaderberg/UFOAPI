/*
 * DATEX II Snapshot Pull API
 *
 * This is DATEX II Snapshot PULL API returning PayloadPublication.
 *
 * The version of the OpenAPI document: 1.0.2
 * Contact: you@your-company.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Org.OpenAPITools.Converters;

namespace Org.OpenAPITools.Models
{ 
    /// <summary>
    /// 
    /// </summary>
    [DataContract]
    public partial class InternationalIdentifier : IEquatable<InternationalIdentifier>
    {
        /// <summary>
        /// Gets or Sets Country
        /// </summary>
        [Required]
        [MaxLength(1024)]
        [DataMember(Name="country", EmitDefaultValue=false)]
        public string Country { get; set; }

        /// <summary>
        /// Gets or Sets NationalIdentifier
        /// </summary>
        [Required]
        [MaxLength(1024)]
        [DataMember(Name="nationalIdentifier", EmitDefaultValue=false)]
        public string NationalIdentifier { get; set; }

        /// <summary>
        /// Gets or Sets InternationalIdentifierExtensionG
        /// </summary>
        [DataMember(Name="internationalIdentifierExtensionG", EmitDefaultValue=false)]
        public Dictionary<string, Object> InternationalIdentifierExtensionG { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class InternationalIdentifier {\n");
            sb.Append("  Country: ").Append(Country).Append("\n");
            sb.Append("  NationalIdentifier: ").Append(NationalIdentifier).Append("\n");
            sb.Append("  InternationalIdentifierExtensionG: ").Append(InternationalIdentifierExtensionG).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="obj">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object obj)
        {
            if (obj is null) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((InternationalIdentifier)obj);
        }

        /// <summary>
        /// Returns true if InternationalIdentifier instances are equal
        /// </summary>
        /// <param name="other">Instance of InternationalIdentifier to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(InternationalIdentifier other)
        {
            if (other is null) return false;
            if (ReferenceEquals(this, other)) return true;

            return 
                (
                    Country == other.Country ||
                    Country != null &&
                    Country.Equals(other.Country)
                ) && 
                (
                    NationalIdentifier == other.NationalIdentifier ||
                    NationalIdentifier != null &&
                    NationalIdentifier.Equals(other.NationalIdentifier)
                ) && 
                (
                    InternationalIdentifierExtensionG == other.InternationalIdentifierExtensionG ||
                    InternationalIdentifierExtensionG != null &&
                    other.InternationalIdentifierExtensionG != null &&
                    InternationalIdentifierExtensionG.SequenceEqual(other.InternationalIdentifierExtensionG)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                var hashCode = 41;
                // Suitable nullity checks etc, of course :)
                    if (Country != null)
                    hashCode = hashCode * 59 + Country.GetHashCode();
                    if (NationalIdentifier != null)
                    hashCode = hashCode * 59 + NationalIdentifier.GetHashCode();
                    if (InternationalIdentifierExtensionG != null)
                    hashCode = hashCode * 59 + InternationalIdentifierExtensionG.GetHashCode();
                return hashCode;
            }
        }

        #region Operators
        #pragma warning disable 1591

        public static bool operator ==(InternationalIdentifier left, InternationalIdentifier right)
        {
            return Equals(left, right);
        }

        public static bool operator !=(InternationalIdentifier left, InternationalIdentifier right)
        {
            return !Equals(left, right);
        }

        #pragma warning restore 1591
        #endregion Operators
    }
}
